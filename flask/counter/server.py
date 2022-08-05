from itertools import count
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "Any string you want5"


@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1
    return render_template("index.html", count= session['count'])

@app.route('/up')
def up():
    session['count'] += 0
    return redirect('/')

@app.route('/add2')
def add_two():
    session['count'] += 1
    return redirect('/')

@app.route('/destroy_session')
def clear():
    session['count'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)


