from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_app.models.user import User

@app.route("/")
def index():
    return render_template("index.html")

#=======================================
# REGISTER ROUTE
#=======================================

@app.route("/register", methods=["POST"])
def register_user():
    #1 validate form info
    if not User.validate_register(request.form):
        return redirect("/")

    #2a convert password via bcrypt
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    #2 collect data from form
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : pw_hash
    }
    #3 run query to database (INSERT)
    new_user_id = User.create_user(data)

    #3a store user id into session
    session['user_id'] = new_user_id


    #4 redirect elsewhere
    return redirect("/dashboard")

#=======================================
# LOGIN ROUTE
#=======================================

@app.route("/login", methods=["POST"])
def login():
    #1 Validate Info
    if not User.validate_login(request.form):
        return redirect("/")

    #2 Query Based on Data
    data = {
        "email" : request.form["email"]
    }
    logged_in_user = User.get_by_email(data)
    #3 Put user_id into session
    session["user_id"] = logged_in_user.id
    #4 Redirect elsewhere
    return redirect("/dashboard")

#=======================================
# DASHBOARD
#=======================================

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("I'm sorry, Dave. I'm afraid I can't do that. Please login or register before entering the site.")
        return redirect("/")
    user_id = session["user_id"]
    return render_template("dashboard.html", logged_user_id = user_id)


#=======================================
# LOGOUT
#=======================================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
