import numpy as np

from keras.models import load_model

# ==================================
# LOAD MODEL
# ==================================

model = load_model(
    "best_diabetes_model.keras"
)

print("Model Loaded Successfully")

# ==================================
# LOAD SCALER
# ==================================

scaler_data = np.load(
    "scaler.npy",
    allow_pickle=True
).item()

mean = scaler_data["mean"]
scale = scaler_data["scale"]

# ==================================
# SAMPLE PATIENT
# ==================================

sample = np.array([
    [6,148,72,35,0,33.6,0.627,50]
])

sample = (
    sample - mean
) / scale

# ==================================
# PREDICT
# ==================================

prediction = model.predict(sample)

probability = prediction[0][0]

print(f"\nDiabetes Probability : {probability:.4f}")

if probability >= 0.5:
    print("Prediction : Diabetic")
else:
    print("Prediction : Non-Diabetic")