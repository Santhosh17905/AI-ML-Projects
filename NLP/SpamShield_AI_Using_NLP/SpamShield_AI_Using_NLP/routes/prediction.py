import logging

from flask import render_template, request
from flask_login import login_required

from database_models import db, Prediction
from services.model_service import predict_spam

def init_prediction(app):

    @app.route("/predict", methods=["GET", "POST"])
    @login_required
    def predict():

        prediction = None
        confidence = None

        if request.method == "POST":

            message = request.form["message"]

            result, conf = predict_spam(message)

            record = Prediction(
                message=message,
                result=result,
                confidence=conf
            )

            db.session.add(record)
            db.session.commit()

            logging.info(
                f"Prediction: {result}"
            )

            prediction = result
            confidence = conf

        return render_template(
            "predict.html",
            prediction=prediction,
            confidence=confidence
        )

    @app.route("/history")
    @login_required
    def history():

        records = Prediction.query.order_by(
            Prediction.id.desc()
        ).all()

        return render_template(
            "history.html",
            history=records
        )