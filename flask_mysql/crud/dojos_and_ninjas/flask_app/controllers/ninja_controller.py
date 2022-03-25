from flask_app import app
from flask import Flask, render_template, request, redirect

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/ninja/new")
def add_ninja():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("add_ninja.html", dojos=dojos)

@app.route("/ninja/create", methods = ["POST"])
def create_ninja():
    data = {
        "dojo_id" : request.form["dojo_id"],
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"]
    }

    Ninja.create_new_ninja(data)

    return redirect(f"/dojo/{data['dojo_id']}")

