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

@app.route("/dashboard/<int:id>")
def index2(id):
    data = {
        "id": id
    }
    # user = User.get_one(data)
    user = User.get_one_with_recipes(data)
    print(user)
    return render_template("dashboard.html", user = user)

# @app.route("/dashboard/<int:id>")
# def show(id):
#     data = {
#         "id": id
#     }
#     user = User.get_one_with_recipes(data)
#     return render_template("dashboard.html", user = user)


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
    # if the passwords matched, we set the user_id into session
    session['user.id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    # never render on a post!!!
    return redirect(f"/dashboard/{user_in_db.id}")



# # ! READ ALL
@app.route("/dashboard/<int:id>")
def read():
    users = User.get_all()
    recipes_per_user = []
    for user in users:
        recipes_per_user.append(User.get_one_with_recipes({'id': user.id}))

    return render_template('index.html', users = User.get_all(), recipes_per_user = recipes_per_user)




@app.route('/logout')
def read():
    users = User.get_all()
    recipes_per_user = []
    for user in users:
        recipes_per_user.append(User.get_one_with_recipes({'id': user.id}))

    return render_template('index.html', users = User.get_all(), recipes_per_user = recipes_per_user)


# ! UPDATE
# @app.route('/edit/<int:id>')
# def edit_user(id):
#     data = {'id':id}
#     return render_template('edit_user.html', user = User.get_one(data))

# @app.route('/update/user', methods = ['post'])
# def update_user():
#     print(request.form)
#     User.update(request.form)
#     return redirect(f"/show/{request.form['id']}")

@app.route("/create_recipe")
def create_recipe():
    print("hello")
    return render_template("create.html")
# def index2():

# ! READ ONE
@app.route("/dashboard/<int:id>")
def show(id):
    data = {
        "id": id
    }
    user = User.get_one_with_recipes(data)
    return render_template("dashboard.html", user = user)


# # # ! Delete 
# @app.route('/delete/<int:id>')
# def delete_user(id):
#     User.destroy({'id': id})
#     return redirect('/')


# @app.route("/create", methods=['post'])
# def create():
#     data = {
#         "first_name": request.form['first_name'],
#         "last_name": request.form['last_name'],
#         "email": request.form['email'], 
#     }
#     recipe = recipe.save(data)
#     return redirect(f"/show/{recipe}")










# @app.route("/create")
# def results():
#     print("hello")
#     return render_template("create.html")
    



# # ! EDIT
# @app.route("/edit/<int:id>")
# def edit_user(id):
#     data = {
#         "id": id
#     }
#     return render_template("edit.html", recipe = recipe.get_one(data))

# @app.route("/update/user", methods = ['post'])
# def update_recipe():
#     recipe.update(request.form)
#     return redirect(f"/show/{request.form['id']}") 

    





@app.route("/")
def home():
    print("hello")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
