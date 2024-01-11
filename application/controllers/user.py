from flask import Blueprint, flash, redirect, request, render_template, jsonify, url_for
from ..models import *
from ..database import db
from flask_login import login_required, current_user, login_manager


user = Blueprint("user", __name__)


standard_questions = [
    "What all to cook?",
    "How much to cook?",
    "When to deliver?",
    "Where to deliver?",
    "How to deliver?",
]


@login_required
@user.route("/user_dashboard", methods=["GET", "POST"])
def user_dashboard():
    if request.method == "POST":
        print(request.form)
        form = request.form
        keys, values = [], []
        for item in form:
            if "key" in item:
                keys.append(request.form.get(item))
            elif "value" in item:
                values.append(request.form.get(item))
        custom_order = dict(zip(keys, values))
    user = Users.query.filter_by(id=current_user.id).first()
    return render_template(
        "user/user_dashboard.html", user=user, questions=standard_questions
    )
