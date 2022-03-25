from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    db = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        
        dojos = []
        for row in results:
            dojos.append(cls(row))
        return dojos 

    @classmethod
    def created_new_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = """SELECT * FROM dojos
        LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(dojo_id)s;"""
        results = connectToMySQL(cls.db).query_db(query, data)

        dojo = cls(results[0])

        for data in results:
            ninja_data = {
                "id" : data["ninjas.id"],
                "first_name" : data["first_name"],
                "last_name" : data["last_name"],
                "age" : data["age"],
                "created_at" : data["ninjas.created_at"],
                "updated_at" : data["ninjas.updated_at"],
                "dojo_id" : data["dojo_id"]
            }

            ninja_instance = ninja.Ninja(ninja_data)

            dojo.ninjas.append(ninja_instance)

        return dojo