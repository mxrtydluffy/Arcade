# import flask to make it a python package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

def create_app():
    """
    Creates flask application & returns it and configures
    variables for flask.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "itsasecret"

    # inside of package need a "." to import
    # if not inside of package "." is not needed
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")


    return app