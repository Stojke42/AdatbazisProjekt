# standard routs for pages
from flask import Blueprint, render_template, request, flash, redirect, url_for
from website import dbapp
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['GET','POST'])
def login():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        user=dbapp.loginuser(email)
        print(user)
        if user!=False:
            if check_password_hash(user["password"], password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)                     #-----------------------------treba class user da dobije
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route("/logout")
def logout():
    return


@auth.route("/sign-up", methods=['GET','POST'])
def sing_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        user=dbapp.existuser(email)
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user=dict(email=email, firstName=firstName, password=generate_password_hash(
                password1, method='sha256'))
            # print(new_user)
            if dbapp.addnewuser(new_user):
                flash('Account created!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash("Account doesn't created! \n Try again later.", category='error')


    return render_template("/signup.html")
