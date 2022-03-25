from flask import Flask, render_template  # Import Flask to allow us to create our app, render_template allows us to return rendered HTML that we created in the index.html in the templates folder
app = Flask(__name__)    # Create a new instance of the Flask class called "app", app is just a name for a variable 

@app.route('/')          # The "@" decorator associates this route with the function immediately following. this is the route method and the ('/') is necessary for every route, set up a routing rule 
def index():     #this function is associated with the app route above and is called when the route is -> changed from hello_world to index for template engines
    #return 'Hello World!'  # Return the string 'Hello World!' as a response -> instead of returning string we return the result of the render_template method, passing in the name of the HTML file
    return render_template('index.html', phrase="hello", times=5) #flask will look into folder called templates and then look for the file name that matches the .html following, take note of the two neww arguments for phrase and times  

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello, " + name.title()

@app.route('/users/<username>/<id>')
def show_user_info(username, id):
    print(id)
    print(username)
    return "username: " + username + ", id: " + id

@app.route('/lists')
def render_lists(): #Soon enough we'll get data from a database, but for now we're hard coding data
    student_info = [
    {'name' : 'Michael', 'age' : 35},
    {'name' : 'John', 'age' : 30 },
    {'name' : 'Mark', 'age' : 25},
    {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)



@app.route('/success')
def success():
    return "success"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode. This shoulds be the very last statement.