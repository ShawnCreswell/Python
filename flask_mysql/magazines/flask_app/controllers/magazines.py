from crypt import methods
import re
from flask_app import app, render_template, redirect, request, session
from flask_app.models.magazine import Magazine
from flask_app.models.user import User





# ! Create magazines
@app.route("/create_magazine")
def resultss():
    print("hello")
    return render_template("create.html", users = User.get_all())

@app.route("/create_a_magazine", methods=['post'])
def create():
    print(request.form)
    user = session['user_id']
    if not Magazine.validate_thought(request.form):
        return redirect("/create_magazine")
    data = {
        "title": request.form['title'],
        "info": request.form['info'],
        "user_id": session['user_id']
    }

    Magazine.save(data)
    return redirect(f"/dashboard/{user}",)

    
# # ! Show
@app.route("/show/<int:id>")
def show1(id):
    data = {
        "id": id, 
    }
    magazine = Magazine.get_one(data)
    return render_template("show.html", magazine = magazine)






@app.route("/edit_magazine/<int:id>")
def edit_magazine(id):
    data = {
        "id": id
    }
    return render_template("edit.html", magazine = Magazine.get_one_magazine(data))


@app.route("/update/magazine", methods=['post'])
def update():
    data = {
        "title": request.form['title'],
        "info": request.form['info'],
        "user_id": session['user_id'],
        "id": request.form['id']
    }

    print(request.form)
    
    Magazine.update2(data)
    user = session['user_id']
    return redirect(f"/dashboard/{user}")



    
# # ! Delete 
@app.route('/delete/<int:id>')
def delete_magazine(id):
    Magazine.destroy({'id': id})
    user = session['user_id']
    return redirect(f"/dashboard/{user}")






if __name__ == "__main__":
    app.run(debug=True)
