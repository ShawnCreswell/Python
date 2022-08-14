import re
from flask_app import app, render_template, redirect, request, session
from flask_app.models.recipe import Recipe
from flask_app.models.user import User





# ! Create recipes
@app.route("/create_recipe")
def results():
    print("hello")
    return render_template("create.html", users = User.get_all())

@app.route("/create_recipe", methods=['post'])
def create():
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instruction": request.form['instruction'], 
        "under": request.form['under'], 
        "date_made": request.form['date_made'], 
        "user_id": session['user.id']
    }
    user = session['user.id']
    Recipe.save(data)
    print(request.form)
    # recipe = Recipe.save(request.form)
    # return redirect(f"/dashboard/{request.form['user_id']}")
    return redirect(f"/dashboard/{user}")


# ! Read all
# @app.route("/recipes")
# def recipes():
#     return render_template('index.html', recipes = Recipe.get_all())

# @app.route("/dashboard/<int:id>")
# def recipes():
#     return render_template('dashboard/{{user.id}}', recipes = Recipe.get_all())

# @app.route("/dashboard/<int:id>")
# def dashboard_recipe(id):
#     recipe = Recipe.get_all()
#     print(recipe)
#     return render_template("dashboard.html", recipe = recipe)



# ! READ ONE
@app.route('/dashboard/recipe/<int:id>')
def show_recipe(id):
    data = {'id': id}
    recipe = Recipe.get_one(data)
    user = User.get_one({'id':recipe.user_id})
    return render_template('show.html', recipe = recipe)

    
# # ! Show
# @app.route("/show/<int:id>")
# def show1(id):
#     data = {
#         "id": id, 
#     }
#     recipe = recipe.get_one(data)
#     return render_template("show.html", recipe = recipe)



# # ! EDIT
# @app.route("/edit/<int:id>")
# def edit_recipe(id):
#     data = {"id": id}
#     return render_template("edit.html", recipe = recipe.get_one(data))

# @app.route("/update/recipe", methods = ['post'])
# def update_recipe():
#     Recipe.update(request.form)
#     return redirect(f"/show/{request.form['id']}") 

    
# # # ! Delete 
# @app.route('/delete/<int:id>')
# def delete_recipe(id):
#     Recipe.destroy({'id': id})
#     return redirect('/')





# @app.route("/")
# def home():
#     print("hello")
#     return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
