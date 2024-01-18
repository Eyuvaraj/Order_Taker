from flask import render_template, request, redirect, url_for, jsonify, flash, session
from flask import current_app as app
import string
from flask_login import (
    user_accessed,
    login_user,
    login_required,
    LoginManager,
    logout_user,
)
from .models import Users, UserLogs
from .database import db
from datetime import datetime

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.session_protection = "strong"


@login_manager.user_loader
def loader_user(user_id):
    return Users.query.filter_by(id=user_id).first()


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = Users.query.filter_by(email=email).first()
        if user is not None and user.password == password:
            if user.role == "admin":
                login_user(user)
                newlog = UserLogs(
                    user_id=user.id, issue="login-success", datetime=datetime.now()
                )
                db.session.add(newlog)
                db.session.commit()
                return redirect(url_for("admin.admin_dashboard"))
            elif user.role == "user":
                login_user(user)
                newlog = UserLogs(
                    user_id=user.id, issue="login-success", datetime=datetime.now()
                )
                db.session.add(newlog)
                db.session.commit()
                return redirect(url_for("user.user_dashboard"))
        elif user is None:
            newlog = UserLogs(
                user_id="Anonymous",
                issue="Invalid user login attempt",
                datetime=datetime.now(),
            )
            db.session.add(newlog)
            db.session.commit()
            flash("User does not exist.")
            return redirect(url_for("login"))
        else:
            flash("Incorrect password, Try again!!")
            newlog = UserLogs(
                user_id=user.id,
                issue="Invalid login credentials",
                datetime=datetime.now(),
            )
            db.session.add(newlog)
            db.session.commit()
            incorrect_attempts = (
                UserLogs.query.filter_by(user_id=user.id)
                .filter_by(issue="Invalid login credentials")
                .count()
            )
            print(incorrect_attempts)
            return redirect(url_for("login"))
    return render_template("auth/login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        username = request.form.get("name")
        user = Users.query.filter_by(email=email).first()
        if email != "" and user is None:
            new_user = Users(email=email, password=password, username=username)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("login"))
        else:
            return redirect(url_for("signup"))
    return render_template("auth/signup.html")


@app.route("/logout")
@login_required
def logout():
    session.clear()
    logout_user()
    return redirect(url_for("index"))


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("login"))
