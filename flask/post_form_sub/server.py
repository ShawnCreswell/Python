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
    session['count'] += 1
    return redirect('/')

@app.route('/clear')
def clear():
    session['count'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)


