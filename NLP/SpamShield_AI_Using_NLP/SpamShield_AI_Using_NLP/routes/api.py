# API routes placeholder
from flask import request, jsonify

from services.model_service import (
    predict_spam
)

def init_api(app):

    @app.route(
        "/api/predict",
        methods=["POST"]
    )
    def api_predict():

        data = request.json

        result, conf = predict_spam(
            data["message"]
        )

        return jsonify({
            "prediction": result,
            "confidence": conf
        })