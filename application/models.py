from .database import db
from flask_login import UserMixin


class users(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False, default="user")


class order(db.Model):
    __tablename__ = "order"
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_naem = db.Column(db.String, nullable=False)
