from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app", app is just a name for a variable 
@app.route('/')          # The "@" decorator associates this route with the function immediately following. this is the route method and the ('/') is necessary for every route, set up a routing rule 
def hello_world():     #this function is associated with the app route above and is called when the route is 
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<username>/<id>')
def show_user_info(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


@app.route('/success')
def success():
    return "success"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode. This shoulds be the very last statement.

