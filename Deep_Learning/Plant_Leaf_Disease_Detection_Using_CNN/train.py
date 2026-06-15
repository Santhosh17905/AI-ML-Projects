import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import GlobalAveragePooling2D
from tensorflow.keras.models import Model

from tensorflow.keras.callbacks import (
    EarlyStopping,
    ReduceLROnPlateau,
    ModelCheckpoint,
    CSVLogger
)

from sklearn.metrics import (
    confusion_matrix,
    classification_report
)

import seaborn as sns

# =====================================
# CONFIG
# =====================================

TRAIN_DIR = "dataset/train"
TEST_DIR = "dataset/test"

IMG_SIZE = 224
BATCH_SIZE = 32
EPOCHS = 20

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# =====================================
# DATA AUGMENTATION
# =====================================

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=25,
    width_shift_range=0.2,
    height_shift_range=0.2,
    zoom_range=0.2,
    shear_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

test_datagen = ImageDataGenerator(
    rescale=1./255
)

train_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

test_generator = test_datagen.flow_from_directory(
    TEST_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    shuffle=False
)

# =====================================
# CLASS INFO
# =====================================

class_names = list(train_generator.class_indices.keys())

print("\nClasses Found:")
for i, cls in enumerate(class_names):
    print(f"{i}: {cls}")

# =====================================
# MODEL
# =====================================

base_model = MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(IMG_SIZE, IMG_SIZE, 3)
)

base_model.trainable = False

x = base_model.output
x = GlobalAveragePooling2D()(x)

x = Dense(
    512,
    activation='relu'
)(x)

x = Dropout(0.4)(x)

outputs = Dense(
    train_generator.num_classes,
    activation='softmax'
)(x)

model = Model(
    inputs=base_model.input,
    outputs=outputs
)

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()

# =====================================
# CALLBACKS
# =====================================

callbacks = [

    EarlyStopping(
        monitor='val_loss',
        patience=5,
        restore_best_weights=True
    ),

    ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.3,
        patience=2
    ),

    ModelCheckpoint(
        os.path.join(
            OUTPUT_DIR,
            "best_model.keras"
        ),
        save_best_only=True
    ),

    CSVLogger(
        os.path.join(
            OUTPUT_DIR,
            "training_log.csv"
        )
    )
]

# =====================================
# TRAIN
# =====================================

history = model.fit(
    train_generator,
    validation_data=test_generator,
    epochs=EPOCHS,
    callbacks=callbacks
)

# =====================================
# EVALUATION
# =====================================

loss, acc = model.evaluate(test_generator)

print("\nTest Accuracy:", round(acc * 100, 2), "%")

# =====================================
# ACCURACY GRAPH
# =====================================

plt.figure(figsize=(10,5))

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])

plt.title("Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")

plt.legend([
    "Train",
    "Validation"
])

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "accuracy_loss.png"
    )
)

plt.close()

# =====================================
# PREDICTIONS
# =====================================

predictions = model.predict(
    test_generator
)

pred_classes = np.argmax(
    predictions,
    axis=1
)

true_classes = test_generator.classes

# =====================================
# CLASSIFICATION REPORT
# =====================================

print("\nClassification Report:\n")

print(
    classification_report(
        true_classes,
        pred_classes,
        target_names=class_names
    )
)

# =====================================
# CONFUSION MATRIX
# =====================================

cm = confusion_matrix(
    true_classes,
    pred_classes
)

plt.figure(figsize=(10,8))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    xticklabels=class_names,
    yticklabels=class_names
)

plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.title(
    "Confusion Matrix"
)

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "confusion_matrix.png"
    )
)

plt.close()

print("\nTraining Complete.")
print("Best Model Saved.")