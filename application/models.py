from .database import db


class order(db.Model):
    __tablename__ = "order"
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_naem = db.Column(db.String, nullable=False)
