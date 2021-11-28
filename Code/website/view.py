# standard routs for pages
from flask import Blueprint, render_template,url_for
from flask_login import login_user, login_required, logout_user, current_user
from website import dbapp
views = Blueprint("views", __name__)

@views.route("/")
@login_required
def home():
    listofperson=dbapp.listperson()
    return render_template("home.html",user=current_user, listofperson=listofperson)