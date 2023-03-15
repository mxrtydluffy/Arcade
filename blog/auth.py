from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    pass

@auth.route("/sign-up")
def logsign_upin():
    pass

@auth.route("/sign-out")
def sign_out():
    pass