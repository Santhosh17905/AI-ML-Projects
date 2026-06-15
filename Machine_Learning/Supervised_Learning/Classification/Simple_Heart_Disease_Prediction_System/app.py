from flask import Flask, render_template, request
import joblib
import numpy as np
from datetime import datetime
import pandas as pd

app = Flask(__name__)

# Load model
model = joblib.load("heart_model.pkl")

FEATURES = [
    "Age",
    "Sex",
    "ChestPainType",
    "RestingBP",
    "Cholesterol",
    "FastingBS",
    "RestingECG",
    "MaxHR",
    "ExerciseAngina",
    "Oldpeak",
    "ST_Slope"
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:

        values = []

        for feature in FEATURES:
            value = request.form.get(feature)
            values.append(float(value))

        data = np.array([values])

        prediction = model.predict(data)[0]

        probability = None

        if hasattr(model, "predict_proba"):
            probability = round(
                max(model.predict_proba(data)[0]) * 100, 2
            )

        if prediction == 1:
            result = "Heart Disease Detected"
            risk_class = "danger"
        else:
            result = "No Heart Disease Detected"
            risk_class = "success"

        timestamp = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

        # Optional prediction logging
        try:
            log = pd.DataFrame([{
                "Time": timestamp,
                "Prediction": result,
                "Confidence": probability
            }])

            log.to_csv(
                "prediction_history.csv",
                mode="a",
                header=False,
                index=False
            )

        except:
            pass

        return render_template(
            "index.html",
            prediction=result,
            confidence=probability,
            risk_class=risk_class,
            timestamp=timestamp
        )

    except Exception as e:
        return render_template(
            "index.html",
            error=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)