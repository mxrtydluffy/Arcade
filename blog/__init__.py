# import flask to make it a python package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    """
    Creates flask application & returns it and configures
    variables for flask.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "itsasecret"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # Telling flask where the database is then initializing it with flask application.
    db.init_app(app)

    # inside of package need a "." to import
    # if not inside of package "." is not needed
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # If user is not imported the database won't store the user.
    from . models import User, Post

    create_database(app)

    # Grants permission to log users in and out of the website.
    login_manager = LoginManager()
    # If user is not logged in and tries to enter a page it will direct to auth.login
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        """
        Can help find user model when logged in.
        Allows to access user information from the database
        given the id of the user
        """
        return User.query.get(int(id))

    return app

def create_database(app):
    """
    Checking if path exists and if it doesn't it creates a database
    """
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Successfully Created Database")