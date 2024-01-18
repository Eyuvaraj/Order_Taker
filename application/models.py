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


class Order_details(db.Model):
    __tablename__ = "order_details"
    order_id = db.Column(db.Integer, db.ForeignKey("orders.order_id"), primary_key=True)
    key = db.Column(db.String, primary_key=True)
    value = db.Column(db.String)


class UserLogs(db.Model):
    __tablename__ = "user_logs"
    log_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    issue = db.Column(db.String)
    datetime = db.Column(db.DateTime)
