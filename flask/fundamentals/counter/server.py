from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'srhgruihj45hti5h'

@app.route('/')
def index():
    print("index worked")
    if 'click' not in session:
        session['click'] = 1
    else:
        session['click'] += 1
    return render_template("index.html")

@app.route('/count', methods=['POST'])
def count_up():
    print("count route worked")
    if request.form['choice']=='click':
        session['click']
    elif request.form['choice']=='reset':
        session['click'] = 0
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()		# clears all keys
    #session.pop('click')		# clears a specific key
    return redirect ('/') 

if __name__ == "__main__":
    app.run(debug=True)