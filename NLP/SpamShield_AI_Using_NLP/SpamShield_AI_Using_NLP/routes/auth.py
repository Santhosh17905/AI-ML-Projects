# Authentication routes placeholder
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required

from database_models import db, User
from utils.security import bcrypt

def init_auth(app):

    @app.route("/register", methods=["GET", "POST"])
    def register():

        if request.method == "POST":

            username = request.form["username"]
            email = request.form["email"]
            password = request.form["password"]

            existing_user = User.query.filter_by(
                email=email
            ).first()

            if existing_user:

                flash(
                    "Email already exists",
                    "danger"
                )

                return redirect(
                    url_for("register")
                )

            hashed_password = bcrypt.generate_password_hash(
                password
            ).decode("utf-8")
            
            print("="*50)
            print("REGISTER")
            print("Original Password:", password)
            print("Generated Hash:", hashed_password)
            print("Hash Length:", len(hashed_password))
            print("="*50)

            new_user = User(
                username=username,
                email=email,
                password=hashed_password
            )

            db.session.add(new_user)
            db.session.commit()

            flash(
                "Registration Successful",
                "success"
            )

            return redirect(
                url_for("login")
            )

        return render_template(
            "register.html"
        )

    @app.route("/login", methods=["GET", "POST"])
    def login():

        if request.method == "POST":

            email = request.form["email"]
            password = request.form["password"]

            user = User.query.filter_by(
                email=email
            ).first()
            
            if user and bcrypt.check_password_hash(user.password, password):
                print(f"LOGIN SUCCESS: {email}")
                login_user(user)
                return redirect(url_for("dashboard"))
            else:
                print(f"LOGIN FAILED: {email}")
                flash("Invalid email or password", "danger")

        return render_template("login.html")

    @app.route("/logout")
    @login_required
    def logout():

        logout_user()

        return redirect(
            url_for("login")
        )