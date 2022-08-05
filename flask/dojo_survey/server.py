from crypt import methods
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "money"


@app.route('/')
def hello_world():

    return render_template("index.html")

@app.route('/', methods=['post'])
def survey():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['textarea'] = request.form['textarea']

    # session['data'] = request.form
    return redirect("/results")

@app.route('/results')
def results():
    print("hello")
    return render_template("results.html")



if __name__ == "__main__":
    app.run(debug=True)
