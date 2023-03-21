from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
@login_required
def home():
    # Changed base.html to index.html for tailwind purposes
    return render_template("home.html", user=current_user)