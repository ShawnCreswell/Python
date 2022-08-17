from ..models.magazine import Magazine
from flask_app import app, render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# ! Home page
@app.route("/")
def index():
    session.clear()
    user = User.get_all()
    print(user)
    return render_template("index.html", user = user)


# ! Create User
@app.route('/register', methods = ['POST'])
def register():
    print(request.form)
    if not User.validate_user(request.form):
        return redirect('/')

    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'], 
        "password": hashed_pw
    }
    user = User.save(data)
    ## Log them in by add them to session
    session['user_id'] = user
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']

    print(hashed_pw)
    return redirect(f"/dashboard/{user}")

# ! Read ALl
@app.route("/dashboard/<int:id>")
def index2(id):
    data = {
        "id": id
    }
    if 'user_id' not in session:
        return redirect('/')
    # user = User.get_one(data)
    user = User.get_one_with_magazines(data)
    magazines =  Magazine.get_all_with_user()
    print(user)
    # return render_template("dashboard.html", magazines=magazines)
    return render_template("dashboard.html", user = user, magazines=magazines)




# ! login user
@app.route('/login', methods = ['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    session['user.id'] = user_in_db.id
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    return redirect(f"/dashboard/{user_in_db.id}")

# ! UPDATE

@app.route("/create_magazine")
def create_magazines():
    print("hello")
    return render_template("create.html")




# ! READ ONE
@app.route("/dashboard/magazine/<int:id>")
def show_magazine(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id,
    }
    users = session['user_id']
    user = User.get_one_with_magazines(data)
    print(user)
    # magazine = Magazine.get_one_magazine(data)
    magazines =  Magazine.get_all_with_user()
    # magazine = Magazine.get_all_with_user()
    print(magazines)

    # user = User.get_one_with_magazines(data)
    # magazines =  Magazine.get_all_with_user()
    return render_template("show.html", magazine = magazines, user=user)



@app.route("/edit/user/<int:id>")
def edit_user(id):
    data = {
        "id": session['user_id']
    }
    print("hello")
    return render_template("edit_user.html", user = User.get_one_with_magazines(data) )

@app.route("/edit/user", methods=['post'])
def update_user():

    users = session['user_id']
    if not User.validate_user(request.form):
        return redirect(f'/edit/user/{users}')
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "id": session['user_id'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'], 
        "password": hashed_pw
    }
    User.update(data)
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']

    print(request.form)
    return redirect(f"/dashboard/{users}")

@app.route("/")
def home():
    print("hello")
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
