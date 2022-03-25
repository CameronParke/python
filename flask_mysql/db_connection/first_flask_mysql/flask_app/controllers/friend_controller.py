from flask_app import app
from flask import render_template, request, redirect, session, flash


# as noted below, import the class from friend.py
from flask_app.models.friend import Friend
from flask_app.models.faction import Faction
# =======================================================
# 'READ'ALL ROUTE / DASHBOARD
# =======================================================
@app.route("/") # when the user visits the root route we want to display all the friends, so our logic will include fetching all the friends from the database and then rendering that data onto our template (the HTML)
def index():
    # call the get_all classmethod like below to get all friends ClassName.get_all
    friends = Friend.get_all()

    # call additional method to grab all factions
    factions = Faction.get_all_factions()
    return render_template("index.html", friends = friends, factions = factions)# the = friends here is the same friends variable from a few lines above that received all the information returned from the friend.py, sends the all_friends to the HTML.
    # all_friends is used in HTML Line 50 as something that can be looped through to produce the results with jinja syntax
            # any time we want to render an HTML page and send the information from our server up to our front end we have to incldue it when we actually render that template. That's why we include all_friends = friends to allow us to use jinja in the front end (HTML) page to pull out all of that information

# =============================================================
# THIS ROUTE IS FROM THE LEARN PLATFORM AND NOT KAYSEE'S VIDEOS
# =============================================================

# @app.route('/create_friend', methods=["POST"]) # what happens: we take in the form data, put it into the data dictionary where the key names line up with the variable names we made in our query class, we process the information with Friend.save(data), adn then we redirect because we redirect on a post
# def create_friend():
#     # First we make a data dictionary from our request.form coming from our template.
#     # The keys in data need to line up exactly with the variables in our query string. 
#     data = {  # all the key names must match the VALUES and variables we name in our friend.py save function query, even more crucial than having our HTML match up with our friend.py VALUES
#         "fname": request.form["fname"],
#         "lname": request.form["lname"],
#         "occ": request.form["occ"],
#         "age": request.form["age"],
#     }
#     # We pass the data dictionary into the save method from the Friend class with the line below
#     Friend.save(data) # we pass in the data information above into the save function for the Friend class.
#     # If we want the ID of the information we receive above we could assign this Friend.save(data) to a variable
#     # Don't forget to redirect after saving to the database
#     return redirect('/')


# =======================================================
# 'READ' ONE ROUTE
# =======================================================

@app.route('/friend/<int:friend_id>')
def one_friend(friend_id):
    data = {
        "friend_id" : friend_id
    }
    one_friend = Friend.get_friend_with_faction(data) # one_friend storing the singular instance we created, now stored in one friend
# to send stuff from the server to the HTML need to include it after the render_template
    return render_template("show_one.html", one_friend = one_friend)

# ==========================================================
# "CREATE" ONE ROUTES, need one to render and one to process
# ==========================================================

@app.route("/friend/new")  # this one renders the page with the form, the form html is passed into render_template
def add_friend():
    factions = Faction.get_all_factions()
    return render_template("add_friend.html", factions = factions)


@app.route("/friend/create", methods=["POST"])  # this one processes the form and submits information to our database
def create_friend():
    #0 validate incoming data
    if not Friend.validate_friend(request.form):
        return redirect("/friend/new")


    #1 - collect the information from our form to send to query
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "occupation" : request.form["occupation"],
        "age" : int(request.form["age"]),
        "faction_id" : request.form["faction_id"]
    }
    #2 - call on query from our model file
    new_friend_id = Friend.create_new_friend(data)

    #3 redirect elswhere once query is done
    return redirect(f"/friend/{new_friend_id}")
