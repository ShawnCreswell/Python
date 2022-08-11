from flask_app import app, render_template, redirect, request
from flask_app.models.ninja import Ninja

# Show
@app.route("/")
def index():
    ninjas = Ninja.get_all()
    print(ninjas)
    return render_template("index.html", ninjas = ninjas)

# ! Create
@app.route("/create", methods=['post'])
def create():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'], 
    }
    ninja = Ninja.save(data)
    return redirect(f"/show/{ninja}")

@app.route("/create")
def results():
    print("hello")
    return render_template("create.html")
    
# ! Show
@app.route("/show/<int:id>")
def show(id):
    data = {
        "id": id
    }
    ninja = Ninja.get_one(data)
    return render_template("show.html", ninja = ninja)



# ! EDIT
@app.route("/edit/<int:id>")
def edit_user(id):
    data = {
        "id": id
    }
    return render_template("edit.html", ninja = Ninja.get_one(data))

@app.route("/update/user", methods = ['post'])
def update_ninja():
    Ninja.update(request.form)
    return redirect(f"/show/{request.form['id']}") 

    
# ! Delete 
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
