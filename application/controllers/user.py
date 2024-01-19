from flask import Blueprint, flash, redirect, request, render_template, jsonify, url_for
from ..models import *
from ..database import db
from flask_login import login_required, current_user
from datetime import datetime

user = Blueprint("user", __name__)


@login_required
@user.route("/user_dashboard", methods=["GET", "POST"])
def user_dashboard():
    date = datetime.now().date()
    if request.method == "POST":
        print(request.form)
        memoryTitle = request.form.get("memoryTitle")
        memory = request.form.get("memory")
        rating = request.form.get("rating")
        new_memory = Memory(
            user_id=current_user.id,
            note_heading=memoryTitle,
            note=memory,
            date=date,
            ratings=rating,
        )
        db.session.add(new_memory)
        db.session.commit()
    return render_template(
        "user/user_dashboard.html", user=current_user, date=date.strftime("%dth %b, %Y")
    )


@login_required
@user.route("/my_memories", methods=["GET"])
def user_memories():
    memories = Memory.query.filter_by(user_id=current_user.id).all()
    return render_template(
        "user/user_memories.html", user=current_user, memories=memories
    )
