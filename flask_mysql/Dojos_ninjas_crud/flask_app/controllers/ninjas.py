from flask_app import app, render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo




# Show
# @app.route("/")
# def index():
#     ninjas = Ninja.get_all()
#     print(ninjas)
#     return render_template("index.html")



# ! Create Ninjas
@app.route("/create_ninja", methods=['post'])
def create():
    dojos = Dojo.get_all()
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'], 
    }
    Ninja.save(data)
    return redirect("/")

@app.route("/create_ninja")
def results():
    print("hello")
    return render_template("create.html")
    
# # ! Show
# @app.route("/show/<int:id>")
# def show1(id):
#     data = {
#         "id": id, 
#     }
#     ninja = Ninja.get_one(data)
#     return render_template("show.html", ninja = ninja)



# # ! EDIT
# @app.route("/edit/<int:id>")
# def edit_user(id):
#     data = {
#         "id": id
#     }
#     return render_template("edit.html", ninja = Ninja.get_one(data))

# @app.route("/update/user", methods = ['post'])
# def update_ninja():
#     Ninja.update(request.form)
#     return redirect(f"/show/{request.form['id']}") 

    
# # ! Delete 
# @app.route('/delete/<int:id>')
# def delete_ninja(id):
#     Ninja.destroy({'id': id})
#     return redirect('/')





# @app.route("/")
# def home():
#     print("hello")
#     return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
