import cv2
import numpy as np
import tensorflow as tf
import os

MODEL_PATH = "outputs/best_model.keras"

model = tf.keras.models.load_model(
    MODEL_PATH
)

# Updated class names to match the 25 classes used during training.
CLASS_NAMES = [
    "Apple___Apple_scab", "Apple___Black_rot", "Apple___Cedar_apple_rust", "Apple___Healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot", "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Healthy", "Corn_(maize)___Northern_Leaf_Blight", "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)", "Grape___Healthy", "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Potato___Early_blight", "Potato___Healthy", "Potato___Late_blight", "Tomato___Bacterial_spot",
    "Tomato___Early_blight", "Tomato___Healthy", "Tomato___Late_blight", "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot", "Tomato___Spider_mites Two-spotted_spider_mite", "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus", "Tomato___Tomato_mosaic_virus"
]

# Corrected path: Changed 'Apple__Apple_scab' to 'Apple___Apple_scab' (3 underscores)
IMAGE_PATH = r"C:\Users\SANTHOSH\Downloads\AI-ML-Projects\Day_15\dataset\test\Apple___Apple_scab\Apple___Apple_scab (1).jpg"

# Safety check: Verify the file exists on disk
if not os.path.exists(IMAGE_PATH):
    print(f"Error: File not found at {IMAGE_PATH}")
    exit()

img = cv2.imread(IMAGE_PATH)

# Safety check: Handle cases where imread returns None
if img is None:
    print(f"Error: Could not decode image at {IMAGE_PATH}. Check file integrity.")
    exit()

# Convert BGR to RGB (OpenCV loads images as BGR by default)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img = cv2.resize(
    img,
    (224,224)
)

img = img.astype("float32") / 255.0

img = np.expand_dims(
    img,
    axis=0
)

pred = model.predict(img)[0]

idx = np.argmax(pred)

disease = CLASS_NAMES[idx]

confidence = pred[idx] * 100

print("\nPrediction")
print("-"*30)

print(
    f"Disease: {disease}"
)

print(
    f"Confidence: {confidence:.2f}%"
)