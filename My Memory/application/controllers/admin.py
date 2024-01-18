from flask import Blueprint, flash, redirect, request, render_template
from ..models import *
from ..database import db
from flask_login import (
    login_required,
    current_user,
)
import requests


admin = Blueprint("admin", __name__)


@login_required
@admin.route("/admin_dashboard", methods=["GET", "POST"])
def admin_dashboard():
    user = Users.query.filter_by(id=current_user.id).first()
    # fastapi_response = requests.get("http://localhost:8000/")
    # print(fastapi_response)
    # if fastapi_response.status_code == 200:
    #     print("success")
    return render_template("admin/admin_dashboard.html", user=user)
