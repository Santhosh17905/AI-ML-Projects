from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_required, current_user
from config import Config
from database_models import db, User, Prediction
from routes.auth import init_auth
from utils.security import bcrypt
import matplotlib.pyplot as plt
import seaborn as sns
import os
import logging

log_dir = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_dir, "app.log"),
    level=logging.INFO
)
from services.analytics import generate_wordcloud
from routes.export import init_export
from routes.api import init_api

from services.analytics import (
    generate_wordcloud
)


app = Flask(__name__)
app.config.from_object(Config)

bcrypt.init_app(app)
db.init_app(app)

with app.app_context():
    db.create_all()

login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))
@app.route("/")
def home():

    return render_template(
        "index.html"
    )

    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    return render_template("home.html")

init_auth(app)
from routes.prediction import (
    init_prediction
)

init_prediction(app)

@app.route("/dashboard")
@login_required
def dashboard():

    total = Prediction.query.count()

    spam_count = Prediction.query.filter_by(
        result="SPAM"
    ).count()

    ham_count = Prediction.query.filter_by(
        result="HAM"
    ).count()

    recent = Prediction.query.order_by(
    Prediction.created_at.desc()
).limit(5)

    # Generate wordcloud from all spam messages
    try:
        all_spam = Prediction.query.filter_by(
            result="SPAM"
        ).all()

        spam_text = " ".join([x.message or "" for x in all_spam])

        if spam_text.strip():
            generate_wordcloud(spam_text)
            wordcloud_url = 'charts/wordcloud.png'
        else:
            wordcloud_url = None
    except Exception:
        wordcloud_url = None

    # Generate pie chart for spam vs ham and save to static/charts/pie.png
    try:
        labels = ["Spam", "Ham"]
        sizes = [spam_count, ham_count]

        plt.figure(figsize=(5, 5))
        plt.pie(sizes, labels=labels, autopct="%1.1f%%")

        chart_dir = os.path.join(app.static_folder, "charts")
        os.makedirs(chart_dir, exist_ok=True)
        chart_path = os.path.join(chart_dir, "pie.png")
        plt.savefig(chart_path)
        plt.close()
    except Exception:
        chart_path = None

    return render_template(
        "dashboard.html",
        total=total,
        spam=spam_count,
        ham=ham_count,
        recent=recent,
        chart_url=("charts/pie.png" if chart_path else None)
    )

# Initialize export routes
init_export(app)
# Initialize API routes
init_api(app)
if __name__ == "__main__":
    app.run(debug=True)