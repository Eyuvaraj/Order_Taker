from flask import Blueprint, flash, redirect, request, render_template, jsonify, url_for
from ..models import *
from ..database import db
from flask_login import login_required, current_user
from datetime import datetime
from sqlalchemy import desc
from sqlalchemy.sql import func

user = Blueprint("user", __name__)


@login_required
@user.route("/post_memory", methods=["POST"])
def post_memory():
    date = datetime.now().date()
    if request.method == "POST":
        memoryTitle = request.form.get("memoryTitle")
        memory = request.form.get("memory")
        rating = request.form.get("rating")
        if rating == "":
            rating = "Average day"

        new_memory = Memory(
            user_id=current_user.id,
            note_heading=memoryTitle,
            note=memory,
            date=date,
            ratings=rating,
        )
        db.session.add(new_memory)
        db.session.commit()
    return redirect(url_for("user.user_dashboard"))


@login_required
@user.route("/user_dashboard", methods=["GET"])
def user_dashboard():
    date = datetime.now().date()

    user_memories_count = Memory.query.filter_by(user_id=current_user.id).count()
    random_memories = []
    if user_memories_count > 2:
        random_memories += (
            Memory.query.filter_by(user_id=current_user.id)
            .order_by(func.random())
            .limit(2)
            .all()
        )

    return render_template(
        "user/user_dashboard.html",
        user=current_user,
        date=date.strftime("%dth %b, %Y"),
        memories=random_memories,
    )


@login_required
@user.route("/my_memories", methods=["GET"])
def user_memories():
    memories = (
        Memory.query.filter_by(user_id=current_user.id)
        .order_by(desc(Memory.memory_id))
        .all()
    )
    return render_template(
        "user/user_memories.html", user=current_user, memories=memories
    )


@login_required
@user.route("/search", methods=["POST"])
def search():
    if request.method == "POST":
        searchTitle = request.form.get("SearchTitle")
        searchDate = request.form.get("DateSearch")
        memories = []
        if searchTitle != "":
            memories += (
                Memory.query.filter_by(user_id=current_user.id)
                .filter(Memory.note_heading.like(f"%{searchTitle}%"))
                .order_by(desc(Memory.memory_id))
                .all()
            )
        elif searchDate != "":
            memories += (
                Memory.query.filter_by(user_id=current_user.id)
                .filter(Memory.date.like(f"%{searchDate}%"))
                .order_by(desc(Memory.memory_id))
                .all()
            )
        return render_template(
            "user/search_results.html",
            user=current_user,
            memories=memories,
            query=[searchTitle, searchDate],
        )
