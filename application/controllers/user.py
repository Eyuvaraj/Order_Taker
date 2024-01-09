from flask import Blueprint, flash, redirect, request, render_template, jsonify, url_for
from ..models import *
from ..database import db
from flask_login import login_required, current_user, login_manager


user = Blueprint("user", __name__)


@login_required
@user.route("/user_dashboard", methods=["GET", "POST"])
def user_dashboard():
    user = Users.query.filter_by(id=current_user.id).first()
    return render_template("user/user_dashboard.html", user=user)
