import pandas as pd
import os

from flask import send_file

from database_models import Prediction

def init_export(app):

    @app.route("/export")

    def export():  # noqa

        data = Prediction.query.all()

        rows = []

        for item in data:

            rows.append({
                "message": item.message,
                "result": item.result,
                "confidence": item.confidence
            })

        df = pd.DataFrame(rows)

        export_path = os.path.join(os.path.dirname(__file__), "..", "exports", "reports.csv")
        
        df.to_csv(
            export_path,
            index=False
        )

        return send_file(
            export_path,
            as_attachment=True
        )