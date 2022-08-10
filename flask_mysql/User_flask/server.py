from flask import Flask, render_template, redirect, request, session
from user import User
app = Flask(__name__)
app.secret_key = "games"

@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", users = users)

# @app.route("/create", methods=['post'])
# def create():
#     session['first_name'] = request.form['first_name']
#     session['last_name'] = request.form['last_name']
#     session['email'] = request.form['email']
#     print(session['first_name'])
#     return redirect("/create")

@app.route("/create", methods=['post'])
def create():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }

    User.save(data)
    return redirect("/")



@app.route("/create")
def results():
    print("hello")
    return render_template("create.html")

@app.route("/")
def home():
    print("hello")
    return redirect("/")
            

if __name__ == "__main__":
    app.run(debug=True)

