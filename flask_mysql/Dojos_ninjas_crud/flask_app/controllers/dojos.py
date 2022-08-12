from flask_app import app, render_template, redirect, request
from flask_app.models.dojo import Dojo


# Show
@app.route("/")
def index():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("index.html", dojos = dojos)



# ! Create Dojos
@app.route("/creates", methods=['post'])
def save():
    dojo = Dojo.save(request.form)
    return redirect("/")



# ! READ ALL
@app.route('/')
def read():
    dojos = Dojo.get_all()
    ninjas_per_dojo = []
    for dojo in dojos:
        ninjas_per_dojo.append(Dojo.get_one_with_ninjas({'id': dojo.id}))

    return render_template('index.html', dojos = Dojo.get_all(), ninjas_per_dojo = ninjas_per_dojo)




@app.route("/create_ninja")
def create_ninja():
    print("hello")
    return render_template("create.html")

# ! UPDATE
@app.route('/edit/<int:id>')
def edit_dojo(id):
    data = {'id':id}
    return render_template('edit_dojo.html', dojo = Dojo.get_one(data))

@app.route('/update/dojo', methods = ['post'])
def update_dojo():
    print(request.form)
    Dojo.update(request.form)
    return redirect(f"/show/{request.form['id']}")

# ! READ ONE
@app.route("/show/<int:id>")
def show(id):
    data = {
        "id": id
    }
    dojo = Dojo.get_one_with_ninjas(data)
    return render_template("show.html", dojo = dojo)

# # ! Delete 
@app.route('/delete/<int:id>')
def delete_dojo(id):
    Dojo.destroy({'id': id})
    return redirect('/')


# @app.route("/create", methods=['post'])
# def create():
#     data = {
#         "first_name": request.form['first_name'],
#         "last_name": request.form['last_name'],
#         "email": request.form['email'], 
#     }
#     ninja = Ninja.save(data)
#     return redirect(f"/show/{ninja}")










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
#     return render_template("edit.html", ninja = Ninja.get_one(data))

# @app.route("/update/user", methods = ['post'])
# def update_ninja():
#     Ninja.update(request.form)
#     return redirect(f"/show/{request.form['id']}") 

    





@app.route("/")
def home():
    print("hello")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
