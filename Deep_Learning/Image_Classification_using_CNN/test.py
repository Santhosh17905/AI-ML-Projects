import os
import cv2
import numpy as np

from tensorflow.keras.models import model_from_json

# ======================================================
# LOAD MODEL
# ======================================================

with open("models/model.json", "r") as json_file:
    model_json = json_file.read()

model = model_from_json(model_json)
model.load_weights("models/model.weights.h5")

print("Model Loaded Successfully")

# ======================================================
# CLASS LABELS
# ======================================================

CLASS_NAMES = {
    0: "Joker",
    1: "Thanos"
}

# ======================================================
# PREDICTION FUNCTION
# ======================================================

def predict_image(image_path):

    image = cv2.imread(image_path)

    if image is None:
        print("Cannot read:", image_path)
        return

    image = cv2.resize(image, (128,128))
    image = image.astype("float32") / 255.0

    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image, verbose=0)

    confidence = float(prediction[0][0])

    if confidence > 0.5:
        label = "Thanos"
        score = confidence
    else:
        label = "Joker"
        score = 1 - confidence

    print("-"*60)
    print(f"Image      : {os.path.basename(image_path)}")
    print(f"Prediction : {label}")
    print(f"Confidence : {score*100:.2f}%")

# ======================================================
# TEST FOLDER
# ======================================================

TEST_FOLDER = "Dataset/test"

for root, dirs, files in os.walk(TEST_FOLDER):

    for file in files:

        if file.lower().endswith(
            (".jpg",".jpeg",".png",".bmp",".webp")
        ):
            predict_image(os.path.join(root,file))