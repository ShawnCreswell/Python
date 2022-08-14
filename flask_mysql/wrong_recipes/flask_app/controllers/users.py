from crypt import methods
import email
from flask_app import app, render_template, redirect, request, session, flash, bcrypt
from flask_app.models.user import User
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)

@app.route('/')
def index():
    session.clear()
    user = User.get_all()
    return render_template('index.html', user = user)    

# ! TO register 
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
    session['user.id'] = user
    session['first_name'] = request.form['first_name']
    print(hashed_pw)
    return redirect(f"/dashboard/{user}")

# ! So user cant get in routes
@app.route('/dashboard')
def dashboard2():
    if 'user_id' not in session:
        return redirect('/logout')
    return f"weclome back"

# ! for create_recipe
@app.route("/create_recipe")
def to_create_recipe():
    return render_template("create.html")


@app.route("/create_recipe", methods = ['POST'])
def create_recipe():
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instruction": request.form['instruction'], 
        "date_made": request.form['date_made'], 
        "user_id": request.form['user_id']
    }
    print(request.form)
    recipe = Recipe.save(data)
    print(data)
    # user = User.get_one()
    # return redirect(f"/dashboard/{user}")
    return redirect("/dashboard")

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
    session['user.id'] = user_in_db.first_name
    # never render on a post!!!
    return redirect(f"/dashboard/{user_in_db.id}")


#!  TO logout user
@app.route('/logout')
def logout():
    # session.clear()
    return redirect('/')

    
# !  Optional
@app.route('/add_recipe/user')
def add_recipe_user():
    pass

@app.route('/update_user', methods = ['POST'])
def update_user():
    pass

if __name__ == "__main__":
    app.run(debug=True)
