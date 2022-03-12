from turtle import color
from flask import Flask, render_template  
app = Flask(__name__)    

print(__name__)

@app.route('/')          
def index():
    return render_template("index.html", num1= 8, num2 = 8)

@app.route('/<int:num>')
def display_ptdeux(num):
    return render_template("index.html", num1 = int(num), num2 = 8)

@app.route('/<int:num1>/<int:num2>')
def display_no3(num1, num2):
    return render_template("index.html", num1 = int(num1), num2 = int(num2))

@app.route('/<int:num1>/<int:num2>/<color0>/<color1>')
def display_color(num1, num2, color0, color1):
    return render_template("index.html", num1 = int(num1), num2 = int(num2), color0 = color0, color1 = color1)

if __name__=="__main__":
    app.run(debug=True)  

