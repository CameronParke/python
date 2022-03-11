from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/dojo')
def say_dojo():
    return "Dojo!"

@app.route('/say/<string:name>')  
def say_hi(name): 
    return f"Hi {name}!"


@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    repeating_word = ''
    for i in range(0, num):
        repeating_word += f"<p>{word}</p>"
        
    return repeating_word

if __name__=="__main__":
    app.run(debug=True) 