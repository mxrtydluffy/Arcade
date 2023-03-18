# "." represents current package we are in. | From init.py import db variable.
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    """
    db.Model represents a database model aka table
    UserMixin easily helps log users in
    """
    # Every table must need at least have one primary key.
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))
    # func.now will fill by default the current time
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

