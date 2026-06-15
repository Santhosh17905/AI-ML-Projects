# Configuration settings for Day29 Email Spam Detection Enterprise
import os

class Config:

    SECRET_KEY = "day29-enterprise-secret"

    BASE_DIR = os.path.abspath(
        os.path.dirname(__file__)
    )

    SQLALCHEMY_DATABASE_URI = \
        "sqlite:///" + os.path.join(
            BASE_DIR,
            "database",
            "spam.db"
        )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MODEL_PATH = os.path.join(
        BASE_DIR,
        "models",
        "spam_model.pkl"
    )

    VECTORIZER_PATH = os.path.join(
        BASE_DIR,
        "models",
        "vectorizer.pkl"
    )