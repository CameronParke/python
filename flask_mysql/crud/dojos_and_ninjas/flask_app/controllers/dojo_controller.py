from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/")
def home_page():
    return redirect("/dojos")

@app.route("/dojos")
def dojos():
    dojos = Dojo.get_all()
    # print(dojos)
    return render_template("index.html", dojos=dojos)

@app.route("/dojo/create", methods=["POST"])
def create_dojo():
    data = {
        "name" : request.form["name"]
    }
    new_dojo_id = Dojo.created_new_dojo(data)
    return redirect("/dojos")

@app.route('/dojo/<int:dojo_id>')
def show_one_dojo(dojo_id):
    data = {
        "dojo_id" : dojo_id
    }
    one_dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template("view_dojo_ninjas.html", one_dojo = one_dojo)
