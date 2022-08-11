from flask_app import app, render_template, redirect, request
from flask_app.models.user import User

# Show
@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", users = users)

# ! Create
@app.route("/create", methods=['post'])
def create():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
    }
    User.save(data)
    return redirect("/")

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
    user = User.get_one(data)
    return render_template("show.html", user = user)



# ! EDIT
@app.route("/edit/<int:id>")
def edit_user(id):
    data = {
        "id": id
    }
    return render_template("edit.html", user = User.get_one(data))

@app.route("/update/user", methods = ['post'])
def update_user():
    User.update(request.form)
    return redirect(f"/show/{request.form['id']}") 

    
# ! Delete 
@app.route('/delete/<int:id>')
def delete_user(id):
    User.destroy({'id': id})
    return redirect('/')





# @app.route("/")
# def home():
#     print("hello")
#     return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
