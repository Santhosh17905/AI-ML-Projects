import os
import struct
import numpy as np
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    Dense,
    Flatten,
    Dropout,
    BatchNormalization
)

from tensorflow.keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint,
    ReduceLROnPlateau
)

# ==========================================
# CONFIG
# ==========================================

DATASET_PATH = "dataset"

TRAIN_IMAGES = os.path.join(
    DATASET_PATH,
    "emnist-balanced-train-images-idx3-ubyte"
)

TRAIN_LABELS = os.path.join(
    DATASET_PATH,
    "emnist-balanced-train-labels-idx1-ubyte"
)

TEST_IMAGES = os.path.join(
    DATASET_PATH,
    "emnist-balanced-test-images-idx3-ubyte"
)

TEST_LABELS = os.path.join(
    DATASET_PATH,
    "emnist-balanced-test-labels-idx1-ubyte"
)

MODEL_PATH = "model/emnist_cnn_model.h5"

os.makedirs("model", exist_ok=True)

# ==========================================
# LOAD IDX FILES
# ==========================================

def load_images(filepath):

    with open(filepath, "rb") as f:

        magic, size, rows, cols = struct.unpack(
            ">IIII",
            f.read(16)
        )

        images = np.frombuffer(
            f.read(),
            dtype=np.uint8
        )

        images = images.reshape(
            size,
            rows,
            cols
        )

    return images


def load_labels(filepath):

    with open(filepath, "rb") as f:

        magic, size = struct.unpack(
            ">II",
            f.read(8)
        )

        labels = np.frombuffer(
            f.read(),
            dtype=np.uint8
        )

    return labels

# ==========================================
# LOAD DATASET
# ==========================================

print("\nLoading EMNIST Dataset...\n")

x_train = load_images(TRAIN_IMAGES)
y_train = load_labels(TRAIN_LABELS)

x_test = load_images(TEST_IMAGES)
y_test = load_labels(TEST_LABELS)

print("Training Images:", x_train.shape)
print("Testing Images :", x_test.shape)

# ==========================================
# PREPROCESSING
# ==========================================

x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

x_train = np.expand_dims(x_train, axis=-1)
x_test = np.expand_dims(x_test, axis=-1)

NUM_CLASSES = len(np.unique(y_train))

print("Classes:", NUM_CLASSES)

# ==========================================
# CNN MODEL
# ==========================================

model = Sequential([

    Conv2D(
        32,
        (3,3),
        activation="relu",
        padding="same",
        input_shape=(28,28,1)
    ),

    BatchNormalization(),

    Conv2D(
        32,
        (3,3),
        activation="relu",
        padding="same"
    ),

    MaxPooling2D((2,2)),
    Dropout(0.25),

    Conv2D(
        64,
        (3,3),
        activation="relu",
        padding="same"
    ),

    BatchNormalization(),

    Conv2D(
        64,
        (3,3),
        activation="relu",
        padding="same"
    ),

    MaxPooling2D((2,2)),
    Dropout(0.25),

    Conv2D(
        128,
        (3,3),
        activation="relu",
        padding="same"
    ),

    BatchNormalization(),

    MaxPooling2D((2,2)),

    Flatten(),

    Dense(
        512,
        activation="relu"
    ),

    Dropout(0.5),

    Dense(
        NUM_CLASSES,
        activation="softmax"
    )
])

# ==========================================
# COMPILE
# ==========================================

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# ==========================================
# CALLBACKS
# ==========================================

callbacks = [

    EarlyStopping(
        patience=5,
        restore_best_weights=True
    ),

    ReduceLROnPlateau(
        factor=0.5,
        patience=2
    ),

    ModelCheckpoint(
        MODEL_PATH,
        save_best_only=True,
        monitor="val_accuracy"
    )
]

# ==========================================
# TRAIN
# ==========================================

history = model.fit(

    x_train,
    y_train,

    validation_data=(
        x_test,
        y_test
    ),

    epochs=20,
    batch_size=128,

    callbacks=callbacks
)

# ==========================================
# EVALUATE
# ==========================================

loss, accuracy = model.evaluate(
    x_test,
    y_test
)

print("\nFinal Accuracy:", accuracy)

# ==========================================
# SAVE
# ==========================================

model.save(MODEL_PATH)

print("\nModel Saved Successfully")
print(MODEL_PATH)