# I can copy and paste this template below into every new project that I have, no need to edit at all, ready to go pre-made

# a cursor is the object we use to interact with the database
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', 
                                    password = '', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        # establish the connection to the database
        self.connection = connection
    # the method to query the database
    def query_db(self, query, data=None):  #The main method we'll be calling on, controls all of our queries, we call upon it with the function in Line 55
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # ==================================================================================
                    # INSERT queries will return the ID NUMBER of the row inserted
                    # ==================================================================================
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # ==================================================================================
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    # ==================================================================================
                    result = cursor.fetchall()
                    return result
                else:
                    # ==================================================================================
                    # UPDATE and DELETE queries will return nothing
                    # ==================================================================================
                    self.connection.commit()
            # except Exception as e:
            #     # if the query fails the method will return FALSE
            #     print("Something went wrong", e)
            #     return False
            # Kaysee reccommended we comment out Lines 41 through 44, controls how our error handling is happening
            # Not bad code or broken, but controls how and where and when the errors are going to be thrown
            # When those lines are in place they allocate your errors to the terminal only
            # Commenting them out will have the errors thrown in the HTML itself, as opposed to thinking things are working when they're not
            # Makes it easier to parse through and troubleshoot errors 
            # =========================================
            finally:
                # close the connection
                self.connection.close() 
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)