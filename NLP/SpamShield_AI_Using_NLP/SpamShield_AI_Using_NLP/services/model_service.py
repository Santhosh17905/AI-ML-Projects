# Model service placeholder
import os
import sys
import pickle
from unittest import result

# Add project root to sys.path to allow imports of 'config' and 'utils' when running this script directly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import Config
from utils.preprocessing import preprocess_text

with open(
    Config.MODEL_PATH,
    "rb"
) as f:
    model = pickle.load(f)

with open(
    Config.VECTORIZER_PATH,
    "rb"
) as f:
    vectorizer = pickle.load(f)

def predict_spam(text):
    text = preprocess_text(text)

    vector = vectorizer.transform([text])

    prediction = model.predict(vector)[0]

    result = (
        "SPAM"
        if prediction == "spam"
        else "HAM"
    )

    probabilities = model.predict_proba(
    vector
)[0]

    confidence = round(
        max(probabilities) * 100,
       2
)
    return result, confidence