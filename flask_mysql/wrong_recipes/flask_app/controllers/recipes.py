from flask_app import app, render_template, redirect, request, session, flash, bcrypt
from flask_app.models.recipe import Recipe
from flask_app.models.user import User



# ! Create
@app.route('/create_recipe')
def index():
    # recipe = Recipe.get_all()
    return render_template('create.html', user = User.get_all())   



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

@app.route("/dashboard")
def dashboard():
    return render_template("/dashboard.html")  

# @app.route("/create_recipe", methods=['post'])
# def create():
#     print(request.form)
#     recipe = Recipe.save(request.form)
#     user = User.get_one()

#     return redirect(f"/dashboard/{request.form['user_id']}")