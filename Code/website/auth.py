# standard routs for pages
from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template("/login.html", text="testing")

@auth.route("/logout")
def logout():
    return

@auth.route("/sign-up")
def sing_up():
    return render_template("/signup.html")