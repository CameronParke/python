from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import friend
from flask import flash

class Faction:
    db = "first_flask"
    def __init__(self, data):
        self.id = data["id"]
        
        self.name = data["name"]
        self.level = data["level"]
        self.date_created = data["date_created"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.friends = [] # placeholder/empty list for multiple friends

    @classmethod
    def created_new_faction(cls, data):
        query = "INSERT INTO factions (name, level, date_created, created_at, updated_at) VALUES ( %(name)s, %(level)s, %(date_created)s, NOW(), NOW());"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def get_all_factions(cls):
        query = "SELECT id, name, level, DATE_FORMAT(date_created,'%M %d, %Y') AS date_created, created_at, updated_at FROM factions;"
        results = connectToMySQL(cls.db).query_db(query)
        
        factions = []
        for row in results:
            factions.append( cls(row) )
        return factions


    @classmethod
    def get_faction_with_friends(cls, data):
        query = """SELECT * FROM factions
                    LEFT JOIN friends ON factions.id = friends.faction_id
                    WHERE factions.id = %(faction_id)s;"""
        results = connectToMySQL(cls.db).query_db(query, data)

# step 1) create an instance of your primary info
# because we did SELECT * FROM factions, "faction" is the primary instance, hence why we are in the faction.py
        faction = cls(results[0]) # create instance of faction
        # step 2) collect the data from the JOINED table
        # we joined onto friends, so that is our secondary info that we need to collect. There are multiple so we need to LOOP.
# ** MAKE SURE that you collect all of the data needed to make an instance!! **
        for data in results:
            friend_data = {
                "id" : data["friends.id"], # on colliding fields that appear in both tables you have to specify which table the info is coming from. ONLY DO THIS FOR THE REDUNDANT FIELDS
                "first_name" : data["first_name"], # DO NOT put the table name for the fields that only appear in the secondary table
                "last_name" : data["last_name"],
                "occupation" : data["occupation"],
                "age" : data["age"],
                "created_at" : data["friends.created_at"],
                "updated_at" : data["friends.updated_at"]
            }

                # step 3) take that collected data and pass it into the related model's class to create an instance.
            friend_instance = friend.Friend(friend_data)

                # step 4) append the new instance into the empty list
            faction.friends.append(friend_instance)
    
                # step 5) return the friend instance which now includes the associated instance inside of it
        return faction

            
                
