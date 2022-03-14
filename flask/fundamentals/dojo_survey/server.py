from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = '58vybghvrvybh'

@app.route('/')
def index():
    print("index worked")
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print("process worked")
    print(request.form)
    session['ninja_name'] = request.form['name']
    session['ninja_location'] = request.form['location']
    session['ninja_language'] = request.form['language']
    session['ninja_comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    print("result worked")
    return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)