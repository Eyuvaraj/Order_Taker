from .database import db
from flask_login import UserMixin


class Users(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False, default="user")


class Orders(db.Model):
    __tablename__ = "orders"
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_name = db.Column(db.String, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
