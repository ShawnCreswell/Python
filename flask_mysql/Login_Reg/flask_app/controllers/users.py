from crypt import methods
import email
from flask_app import app, render_template, redirect, request, session
from flask_app.models.user import User


@app.route('/')
def index():
    user = User.get_all()
    return render_template('index.html', user = user)    

# ! TO register 
@app.route('/register', methods = ['POST'])
def register():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'], 
        "password": request.form['password']
    }
    user = User.save(data)
    # if not User.validate_user(request.form):
    #     return redirect('/')
    ## Log them in by add them to session
    return redirect(f"/show/{user}")

@app.route("/show/<int:id>")
def dashboard(id):
    data = {
        "id":id
    }
    user = User.get_one(data)
    return render_template('show.html', user = user)    


# ! login user
@app.route('/login', methods = ['POST'])
def login():

    print(session)
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    ## check database for email they enter
    if not User.validate_user_email(request.form):
        return redirect('/')
    ## check password they supply matches the hash in the database
    if not User.validate_user_password(request.form):
        return redirect('/')
    
    
    # return redirect(f"/show/{request.form['id']}")
    return redirect("/")


#!  TO logout user
@app.route('/logout')
def logout():
    session.clear()
    pass
    return redirect('/')

    
# !  Optional
@app.route('/edit/user')
def edit_user():
    pass

@app.route('/update_user', methods = ['POST'])
def update_user():
    pass

if __name__ == "__main__":
    app.run(debug=True)
