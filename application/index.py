from flask import render_template, request, redirect, url_for, jsonify, flash, session
from flask import current_app as app
from flask_login import (
    user_accessed,
    login_user,
    login_required,
    LoginManager,
    logout_user,
)
from .models import Users
from .database import db

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
                return redirect(url_for("admin.admin_dashboard"))
            elif user.role == "user":
                login_user(user)
                return redirect(url_for("user.user_dashboard"))
        elif user is None:
            flash("User does not exist.")
            return redirect(url_for("login"))
        else:
            flash("Incorrect password, Try again!! or ")
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
