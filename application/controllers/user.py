from flask import Blueprint, flash, redirect, request, render_template
from ..models import *
from ..database import db
from flask_login import (
    login_required,
    current_user,
)


user = Blueprint("user", __name__)


@login_required
@user.route("/user_dashboard", methods=["GET", "POST"])
def user_dashboard():
    return render_template("user/user_dashboard.html")
