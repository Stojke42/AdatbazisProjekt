# standard routs for pages


from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['POST'])
def login():
    return render_template("/login.html", text="testing")


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

        if len(email) < 4:
            flash("email must be greater  than 4 char", category='error')
        else:
            flash("acc created", category="success")


    return render_template("/signup.html")
