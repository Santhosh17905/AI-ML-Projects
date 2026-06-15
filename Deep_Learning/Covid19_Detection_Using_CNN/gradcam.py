import tensorflow as tf
import numpy as np
import cv2

def get_gradcam_sequential(model, img_array):
    # 1. Find the last convolutional layer by checking the layer type
    last_conv_layer = None
    parent_layer = None
    
    
    # We look for any 2D Convolutional layer
    for layer in reversed(model.layers):
        if isinstance(layer, tf.keras.layers.Conv2D):
            last_conv_layer = layer
            break

    # Fallback: if it's a nested model (like ResNet/MobileNet), search inside sub-layers
    if last_conv_layer is None:
        for layer in reversed(model.layers):
            if hasattr(layer, 'layers'): # Check if it's a nested model
                for sub_layer in reversed(layer.layers):
                    if isinstance(sub_layer, tf.keras.layers.Conv2D):
                        last_conv_layer = sub_layer
                        parent_layer = layer
                        break
            if last_conv_layer: break

    if last_conv_layer is None:
        raise ValueError("Could not find a Conv2D layer in the model.")

    # 2. Create the Grad-CAM model
    # If the layer is inside a nested model (like ResNet inside Sequential),
    # we need to rebuild the graph from the nested model's input.
    if parent_layer is not None:
        # 1. Create an inner model that outputs both the conv output and the inner model's final output
        inner_model = tf.keras.models.Model(
            inputs=parent_layer.inputs,
            outputs=[last_conv_layer.output, parent_layer.outputs[0]]
        )

        # 2. Reconstruct the full model flow
        parent_idx = -1
        for i, layer in enumerate(model.layers):
            if layer == parent_layer:
                parent_idx = i
                break

        # Start from the main model input
        x = model.inputs[0]
        
        # Apply layers before parent_layer (if any)
        for layer in model.layers[:parent_idx]:
            x = layer(x)
            
        # Apply the inner model
        conv_output, x = inner_model(x)
        
        # Apply layers after parent_layer
        for layer in model.layers[parent_idx+1:]:
            x = layer(x)
            
        grad_model = tf.keras.models.Model(
            inputs=model.inputs,
            outputs=[conv_output, x]
        )
    else:
        grad_model = tf.keras.models.Model(
            inputs=model.inputs,
            outputs=[last_conv_layer.output, model.output]
        )

    # 3. Record the gradients
    with tf.GradientTape() as tape:
        last_conv_layer_output, preds = grad_model(img_array)
        class_idx = tf.argmax(preds[0])
        loss = preds[:, class_idx]

    # 4. Compute gradients and generate heatmap
    grads = tape.gradient(loss, last_conv_layer_output)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    
    last_conv_layer_output = last_conv_layer_output[0]
    heatmap = last_conv_layer_output @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)

    # Normalize
    heatmap = tf.maximum(heatmap, 0) / (tf.math.reduce_max(heatmap) + 1e-10)
    return heatmap.numpy()

def overlay_heatmap(heatmap, image, alpha=0.4, colormap=cv2.COLORMAP_JET):
    # Resize heatmap to match image dimensions
    heatmap = cv2.resize(heatmap, (image.shape[1], image.shape[0]))

    # Rescale heatmap to 0-255
    heatmap = np.uint8(255 * heatmap)
    jet = cv2.applyColorMap(heatmap, colormap)
    jet = cv2.cvtColor(jet, cv2.COLOR_BGR2RGB)

    # Ensure original image is uint8
    if image.max() <= 1.0:
        image = (image * 255).astype(np.uint8)
    
    # Remove batch dimension if present
    if len(image.shape) == 4:
        image = image[0]
    
    # Superimpose
    output = cv2.addWeighted(image, 1 - alpha, jet, alpha, 0)
    return output