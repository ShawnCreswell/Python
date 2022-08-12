import re
from flask_app import app, render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo



@app.route("/create_ninja")
def results():
    print("hello")
    return render_template("create.html", dojos = Dojo.get_all())


# ! Create Ninjas
@app.route("/create_ninja", methods=['post'])
def create():
    print(request.form)
    ninja = Ninja.save(request.form)
    return redirect(f"/")
    # return redirect(f"/show/{request.form['id']}")

# ! Read all
@app.route("/ninjas")
def ninjas():
    return render_template('index.html', ninjas = Ninja.get_all())

# ! READ ONE
@app.route('/show/ninja/<int:id>')
def show_ninja(id):
    data = {'id': id}
    ninja = Ninja.get_one(data)
    dojo = Dojo.get_one({'id':ninja.dojo_id})
    return render_template('show.html', ninja = ninja)

    
# # ! Show
# @app.route("/show/<int:id>")
# def show1(id):
#     data = {
#         "id": id, 
#     }
#     ninja = Ninja.get_one(data)
#     return render_template("show.html", ninja = ninja)



# # ! EDIT
@app.route("/edit/<int:id>")
def edit_ninja(id):
    data = {"id": id}
    return render_template("edit.html", ninja = Ninja.get_one(data))

@app.route("/update/ninja", methods = ['post'])
def update_ninja():
    Ninja.update(request.form)
    return redirect(f"/show/{request.form['id']}") 

    
# # ! Delete 
@app.route('/delete/<int:id>')
def delete_ninja(id):
    Ninja.destroy({'id': id})
    return redirect('/')





# @app.route("/")
# def home():
#     print("hello")
#     return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
