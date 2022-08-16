import re
from flask_app import app, render_template, redirect, request, session
from flask_app.models.comment import Comment
from flask_app.models.user import User





# ! Create comments
# @app.route("/create_comment")
# def resultss():
#     print("hello")
#     return render_template("create.html", users = User.get_all())

@app.route("/create_a_comment", methods=['post'])
def create():
    print(request.form)
    user = session['user_id']
    if not Comment.validate_thought(request.form):
        return redirect(f"/dashboard/{user}")
    data = {
        "text": request.form['text'], 
        "user_id": session['user_id']
    }
    Comment.save(data)
    # comment = Comment.save(request.form)
    # return redirect(f"/dashboard/{request.form['user_id']}")
    return redirect(f"/dashboard/{user}")


# ! Read all
@app.route("/dashboard/<int:id>")
def index3(id):
    data = {
        "id": id
    }
    # user = User.get_one(data)
    user = User.get_one_with_comments(data)
    comments =  Comment.get_all_with_user()
    # user_names = User.get_one_name(data)
    # print("****************")
    # print(user_names)
    print(user)
    return render_template("dashboard.html", user = user, comments=comments)

# @app.route("/dashboard/<int:id>")
# def dashboard_comment(id):
#     comment = comment.get_all()
#     print(comment)
#     return render_template("dashboard.html", comment = comment)



# # ! READ ONE
# @app.route("/dashboard/comment/<int:id>")
# def show_comment(id):
#     data = {'id': id}
#     comment = comment.get_one(data)
#     return render_template('show.html', comment = comment)

    
# # ! Show
# @app.route("/show/<int:id>")
# def show1(id):
#     data = {
#         "id": id, 
#     }
#     comment = comment.get_one(data)
#     return render_template("show.html", comment = comment)





# # ! EDIT
# @app.route("/edit/<int:id>")
# def edit_comment(id):
#     data = {"id": id}
#     return render_template("edit.html", comment = comment.get_one(data))

# @app.route("/update/comment", methods = ['post'])
# def update_comment():
#     comment.update(request.form)
#     return redirect(f"/show/{request.form['id']}")

@app.route("/edit_comment/<int:id>")
def edit_comment(id):
    data = {
        "id": id
    }
    return render_template("edit.html", comment = Comment.get_one_comment(data))

# @app.route("/edit_comment/<int:id>")
# def edit_comment2(id):
#     data = {
#         "id": id
#     }
#     return redirect("/dashboard/{{user_id}}")




@app.route("/update/comment", methods=['post'])
def update():
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instruction": request.form['instruction'],
        "date_made": request.form['date_made'],
        "under": request.form['under'],
        "user_id": session['user_id'],
        "id": request.form['id']
    }

    print(request.form)
    
    Comment.update2(data)
    user = session['user_id']
    return redirect(f"/dashboard/{user}")



    
# # ! Delete 
@app.route('/delete/<int:id>')
def delete_comment(id):
    Comment.destroy({'id': id})
    user = session['user_id']
    return redirect(f"/dashboard/{user}")





# @app.route("/")
# def home():
#     print("hello")
#     return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
