# "." represents current package we are in. | From init.py import db variable.
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    """
    db.Model represents a database model aka table
    UserMixin easily helps log users in
    - one:many relationship | one user can have many posts
    """
    # Every table must need at least have one primary key.
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))
    # func.now will fill by default the current time
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    # backref references the user that created the post.
    # Passive delete allows of the posts to be deleted when object is deleted.
    posts = db.relationship('Post', backref='user', passive_deletes=True)

class Post(db.Model):
    """
    Regular database model that doesn't need UserMixin.
    Need a p[roper way to relate tables together with users.
    """
    id = db.Column(db.Integer, primary_key=True)
    text= db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    # CASACADE and delete the post what the user has.
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
