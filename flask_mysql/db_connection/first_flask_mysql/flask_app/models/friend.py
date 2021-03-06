# this is a model file. model file shoud always be lowercase and singular. just like class in general is uppercase singular
# model file controls what the database is modelled after. should reflect almost exactly if not exactly what ypur database looks like

# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import faction
from flask import flash 
import re # the regex module
# create a regular expression object that we'll use later
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-z0-9._-]+\.[a-zA-z]+$')

# model the class after the friend table from our database
class Friend:  # everything after the class file should be indented until exiting the class
    db = "first_flask"  # This is another way to declare which schema to pull the data from
    def __init__(self, data ): #the init data should reflect the databse exactly. this is how we pull raw data and pass it into our instances to create individual instances themselves
        # reminder, the __init__ is a CONSTRUCTOR for the individual instances.
        #the data[''] line below will match your column names exactly
        self.id = data["id"]
        
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.occupation = data["occupation"]
        self.age = data["age"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.faction = {} # placeholder for 1 faction

# ================================================
# VALIDATIONS
# ================================================

    @staticmethod  # staticmethod doesn't get passed class, no default argument to be passed in
    def validate_friend(form_data):
        is_valid = True # we assume this is true, we check for negative cases
        
        if len(form_data["first_name"]) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False

        if len(form_data["last_name"]) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
            
        if len(form_data["occupation"]) < 5:
            flash("Occupation must be at least 5 characters.")
            is_valid = False
        
        if not EMAIL_REGEX.match(form_data["occupation"]):
            flash("Please enter a valid email!")
            is_valid = False

        if len(form_data["age"]) < 1: # confirm that they entered a number
            flash("Please enter an age!")
            is_valid = False
        elif int(form_data["age"]) < 14: # verify that they entered an age that satisfies any age minimums to visit the site
            flash("Must be at least 14 years old to enter site!")
        
            
        return is_valid   # should always end with return is_valid

# ================================================
# QUERY Methods
# ================================================

    # Now below we use class methods to query our database
    @classmethod  #every query we write will use a class method. we do this to make everything below available to the overall class 
    def get_all(cls): # the main function of the get_all function is to return everything inside of the current schema, and this will come into play from our server.py file.
        query = "SELECT * FROM friends;" # here's what the actual query that will be called is
        # note below and make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db).query_db(query) # here is how we actually call the query
        print(results)
        # results will store a list of dictionaries
        # As noted below, create an empty list to append our instances of friends,
        # And the lines below will parse that data into actual isntances in our project
        friends = []
        # Use the for loop below to iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) ) # for each one of the dictionaries in the friends list of dicionaries in LINE 30 we will create an instance based off the data. it gets translated up to the __init__ method above in  LINE 9 and it creates an instance based off the info in the database as we parse through the loop in these LINEs here
        return friends  # gets returned to friends = Friend.get_all() in server.py on @app.route('/')

    @classmethod
    def get_one_friend(cls, data): 
        query = "SELECT * FROM friends WHERE id = %(friend_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0]) 

    @classmethod
    def create_new_friend(cls, data):
        query = "INSERT INTO friends (first_name, last_name, occupation, age, created_at, updated_at, faction_id) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, %(age)s, NOW(), NOW(), %(faction_id)s);"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def get_friend_with_faction(cls, data):
        query = """SELECT * FROM friends
                JOIN factions ON friends.faction_id = factions.id
                WHERE friends.id = %(friend_id)s;"""

        results = connectToMySQL(cls.db).query_db(query, data)
# step 1) create an instance of your primary info
# because we did SELECT * FROM friends, "friend" is the primary info, hence why we are in the friend.py
        friend = cls(results[0]) # create instance of friend

# step 2) collect the data from the JOINED table
# we joined onto factions, so that is our secondary info that we need to collect. There are multiple so we need to LOOP.
# ** MAKE SURE that you collect all of the data needed to make an instance!! **

        faction_data = {
            "id" : results[0]["factions.id"],
            "name" : results[0]["name"],
            "level" : results[0]["level"],
            "date_created" : results[0]["date_created"],
            "created_at" : results[0]["factions.created_at"],
            "updated_at" : results[0]["factions.updated_at"]
        }
# step 3) take that collected data and pass it into the related model's class to create an instance.
        faction_instance = faction.Faction(faction_data)

# step 4) replace the placeholder with the attached instance
        friend.faction = faction_instance
    
# step 5) return the friend instance which now includes the associated instance inside of it
        return friend

    

    # @classmethod
    # def save(cls, data ): # make sure we have a @classmethod on our Friend class that actually saves it to the database. every time we query the database we will create a classmethod on that class. this is the @classmethod of save for friend
    #     query = "INSERT INTO friends ( first_name , last_name , occupation , age, created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(occ)s , %(age)s , NOW() , NOW() );"
    #     # data is a dictionary that will be passed into the save method from server.py
    #     # return connectToMySQL('cls.db').query_db( query, data )
    #     return connectToMySQL(cls.db).query_db( query, data ) # when we create something in the database it will send us back the "d "f that row so if you wanted to use that id to go to a page for only that 1 friend you have that id available to you. This return on LINE 41 would return an integer, being whatever ID we just created in the database.

        # in the return statement above results is a list of dictionaries, results[0] will return the first dictionary in the list
# Line 24 is declaring the SQL text that will be sent back to database to run a query
# In Line 26 we declare the name of our schema database within the () following the connectToMySQL function
# In example: connectToMySQL(SCHEMA NAME GOES HERE)
# Alternatively, you can declare your database at the top of your class attributes above the def__init__
# To do so you type db = "SCHEMA_NAME_GOES_HERE", and then in Line 26 you can use (cls.db) instead of ('first_flask')
# Some people prefer this way because they only have to declare it once and not worry about it elsewhere
# And then you can copy and paste Line 26 across EVERY file and not worry about it being incorrect

# self is to instance (self allows an instance to refer to itself)
# as cls is to class (cls is referring to whatever class you are currently inside of)
# If it's a @classmethod the rule is we always have to pass in cls ie: (cls)
# When we say coonectToMYSQL(cls.db) it means whatever class we are currently inside of, I'm referring to this class's db variable
# Because it's defined outside of our __init__ method that db variable is a class variable or class attribute
# So we have to refer to the class and then the attribute itself.
