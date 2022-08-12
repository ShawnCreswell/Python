from crypt import methods
from flask_app import app, render_template, redirect, request, session
from flask_app.models.user import User


@app.route('/')
def index():
    return render_template('index.html')    

# ! TO register 
@app.route('/register', methods = ['POST'])
def register():
    ## Validate
    ## Add user to database
    ## Log them in by add them to session
    pass
    return redirect('/dashboard')

# ! login user
@app.route('/login', methods = ['POST'])
def login():
    ## check database for email they enter
    ## check password they supply matches the hash in the database
    ## Log in the user by adding to session
    
    pass
    return redirect('/dashboard')

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
