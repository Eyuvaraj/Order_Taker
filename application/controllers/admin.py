from flask import Blueprint, flash, redirect, request, render_template
from ..models import *
from ..database import db
from flask_login import (
    login_required,
    current_user,
)


admin = Blueprint("admin", __name__)


@login_required
@admin.route("/admin_dashboard", methods=["GET", "POST"])
def admin_dashboard():
    user = Users.query.filter_by(id=current_user.id).first()
    return render_template("admin/admin_dashboard.html", user=user)
