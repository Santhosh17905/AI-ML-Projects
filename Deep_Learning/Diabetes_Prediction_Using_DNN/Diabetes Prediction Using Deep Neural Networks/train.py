import os
os.environ["KERAS_BACKEND"] = "tensorflow"


import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization
from keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint,
    ReduceLROnPlateau
)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score
)

# ==================================================
# CONFIG
# ==================================================

DATASET_PATH = DATASET_PATH = r"C:\Users\SANTHOSH\Downloads\AI-ML-Projects\Day_11\Day_11\pima-indians-diabetes.csv"
MODEL_PATH = "best_diabetes_model.keras"
SCALER_PATH = "scaler.npy"

RANDOM_STATE = 42

# ==================================================
# LOAD DATA
# ==================================================

print("\nLoading Dataset...")

dataset = np.loadtxt(DATASET_PATH, delimiter=",")

X = dataset[:, 0:8]
y = dataset[:, 8]

print(f"Dataset Shape : {dataset.shape}")
print(f"Features      : {X.shape}")
print(f"Labels        : {y.shape}")

# ==================================================
# TRAIN TEST SPLIT
# ==================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=RANDOM_STATE,
    stratify=y
)

# ==================================================
# FEATURE SCALING
# ==================================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

np.save(SCALER_PATH, {
    "mean": scaler.mean_,
    "scale": scaler.scale_
})

print("Scaler saved.")

# ==================================================
# BUILD MODEL
# ==================================================

model = Sequential([
    
    Dense(
        64,
        activation="relu",
        input_shape=(8,)
    ),

    BatchNormalization(),

    Dropout(0.30),

    Dense(
        32,
        activation="relu"
    ),

    BatchNormalization(),

    Dropout(0.25),

    Dense(
        16,
        activation="relu"
    ),

    Dense(
        1,
        activation="sigmoid"
    )
])

# ==================================================
# COMPILE
# ==================================================

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# ==================================================
# CALLBACKS
# ==================================================

early_stop = EarlyStopping(
    monitor="val_loss",
    patience=15,
    restore_best_weights=True
)

checkpoint = ModelCheckpoint(
    MODEL_PATH,
    monitor="val_accuracy",
    save_best_only=True,
    verbose=1
)

reduce_lr = ReduceLROnPlateau(
    monitor="val_loss",
    factor=0.5,
    patience=5,
    verbose=1
)

# ==================================================
# TRAIN
# ==================================================

history = model.fit(
    X_train,
    y_train,
    validation_split=0.2,
    epochs=200,
    batch_size=16,
    callbacks=[
        early_stop,
        checkpoint,
        reduce_lr
    ],
    verbose=1
)

# ==================================================
# EVALUATE
# ==================================================

print("\nEvaluating Model...")

loss, accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print(f"\nTest Accuracy : {accuracy*100:.2f}%")

# ==================================================
# PREDICTIONS
# ==================================================

pred_prob = model.predict(X_test)

predictions = (
    pred_prob > 0.5
).astype(int)

# ==================================================
# METRICS
# ==================================================

print("\nClassification Report")
print(
    classification_report(
        y_test,
        predictions
    )
)

print("\nConfusion Matrix")
print(
    confusion_matrix(
        y_test,
        predictions
    )
)

auc = roc_auc_score(
    y_test,
    pred_prob
)

print(f"\nROC AUC Score : {auc:.4f}")

print("\nTraining Completed Successfully")