from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    # Changed base.html to index.html for tailwind purposes
    return render_template("home.html")