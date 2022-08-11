from crypt import methods
from unittest import result
from flask_app import app, render_template, redirect, request

from flask_app.models.user import User

@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", users = users)

@app.route("/create", methods=['post'])
def create():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
    }
    User.save(data)
    return redirect("/")


@app.route("/show/<int:id>")
def show(id):
    data = {
        "id": id
    }
    user = User.get_one(data)
    return render_template("show.html", user = user)

@app.route("/create")
def results():
    print("hello")
    return render_template("create.html")

@app.route("/")
def home():
    print("hello")
    return redirect("/")

# @app.route("/", methods=['post'])
# def display():
    
#     return redirect("/show")
            



@app.route("/show/<int:id>/edit", methods = ['post'])
def create2():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    User.save(data)
    return redirect("/")

@app.route("/show/<int:id>/edit")
def edit(id):
    data = {
        "id": id
    }
    user = User.get_one(data)

    return render_template("edit.html", user = user)
    

if __name__ == "__main__":
    app.run(debug=True)
