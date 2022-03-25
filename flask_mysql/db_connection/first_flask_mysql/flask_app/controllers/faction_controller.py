from flask_app import app
from flask import render_template, request, redirect, session

from flask_app.models.friend import Friend
from flask_app.models.faction import Faction


# ==========================================================
# "CREATE" ONE ROUTES, need one to render and one to process
# ==========================================================

@app.route('/faction/new')
def new_faction():
    return render_template('add_faction.html')


@app.route('/faction/create', methods = ["POST"])
def create_faction():
    data = {
        "name" : request.form["name"],
        "level" : request.form["level"],
        "date_created" : request.form["date_created"]
    }
    new_faction_id = Faction.created_new_faction(data)
    return redirect('/')


# =======================================================
# 'READ' ONE ROUTE / SHOW ONE ROUTE
# =======================================================

@app.route('/faction/<int:faction_id>')
def show_one_faction(faction_id):
    data = {
        "faction_id" : faction_id
    }
    one_faction = Faction.get_faction_with_friends(data) # one_faction storing the singular instance we created, now stored in one faction
    return render_template("show_one_faction.html", one_faction = one_faction)
# # to send stuff from the server to the HTML need to include it after the render_template
#     return render_template("show_one.html", one_faction = one_faction)
