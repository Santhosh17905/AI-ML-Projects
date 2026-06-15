import os
import json
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    Dense,
    Flatten,
    Dropout,
    BatchNormalization
)
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint,
    ReduceLROnPlateau
)

# ======================================================
# CONFIG
# ======================================================

IMG_SIZE = 128
BATCH_SIZE = 16
EPOCHS = 30

TRAIN_DIR = "Dataset/train"
VAL_DIR = "Dataset/val"

os.makedirs("models", exist_ok=True)
os.makedirs("plots", exist_ok=True)

# ======================================================
# DATA AUGMENTATION
# ======================================================

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    zoom_range=0.20,
    width_shift_range=0.20,
    height_shift_range=0.20,
    horizontal_flip=True,
    fill_mode='nearest'
)

val_datagen = ImageDataGenerator(rescale=1./255)

train_set = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='binary'
)

val_set = val_datagen.flow_from_directory(
    VAL_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='binary'
)

print("\nClass Mapping:")
print(train_set.class_indices)

# ======================================================
# MODEL
# ======================================================

model = Sequential([

    Conv2D(32, (3,3), activation='relu',
           input_shape=(IMG_SIZE, IMG_SIZE, 3)),
    BatchNormalization(),
    MaxPooling2D(),

    Conv2D(64, (3,3), activation='relu'),
    BatchNormalization(),
    MaxPooling2D(),

    Conv2D(128, (3,3), activation='relu'),
    BatchNormalization(),
    MaxPooling2D(),

    Flatten(),

    Dense(256, activation='relu'),
    Dropout(0.5),

    Dense(128, activation='relu'),
    Dropout(0.3),

    Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.summary()

# ======================================================
# CALLBACKS
# ======================================================

callbacks = [

    EarlyStopping(
        monitor='val_loss',
        patience=5,
        restore_best_weights=True
    ),

    ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.5,
        patience=2
    ),

    ModelCheckpoint(
        "models/best_model.keras",
        monitor='val_accuracy',
        save_best_only=True
    )
]

# ======================================================
# TRAIN
# ======================================================

history = model.fit(
    train_set,
    validation_data=val_set,
    epochs=EPOCHS,
    callbacks=callbacks
)

# ======================================================
# SAVE MODEL
# ======================================================

with open("models/model.json", "w") as json_file:
    json_file.write(model.to_json())

model.save_weights("models/model.weights.h5")

print("\nModel Saved Successfully")

# ======================================================
# ACCURACY PLOT
# ======================================================

plt.figure(figsize=(8,5))
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.legend(['Train','Validation'])
plt.title("Accuracy")
plt.savefig("plots/accuracy.png")
plt.close()

# ======================================================
# LOSS PLOT
# ======================================================

plt.figure(figsize=(8,5))
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['Train','Validation'])
plt.title("Loss")
plt.savefig("plots/loss.png")
plt.close()

print("Training Completed")