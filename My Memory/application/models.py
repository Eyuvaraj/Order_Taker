from .database import db
from flask_login import UserMixin


class Users(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False, default="user")


class Memory(db.Model):
    __tablename__ = "memory"
    memory_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)


class User_Memory(db.Model):
    __tablename__ = "user_memory"
    memory_id = db.Column(
        db.Integer, db.ForeignKey("memory.memory_id"), primary_key=True
    )
    note_heading = db.Column(db.String, primary_key=True)
    note = db.Column(db.String)
    date = db.Column(db.Date)


class UserLogs(db.Model):
    __tablename__ = "user_logs"
    log_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    issue = db.Column(db.String)
    datetime = db.Column(db.DateTime)
