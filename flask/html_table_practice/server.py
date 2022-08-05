from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    users = [
        {'first_name': 'Dashawn', 'last_name': 'Creswell'},
        {'first_name': 'Omar', 'last_name': 'Hizzy'},
        {'first_name': 'Him', 'last_name': 'Gojo'},
        {'first_name': 'Ben', 'last_name': 'Dee'}
    ]
    return render_template("index.html", users = users)


if __name__ == "__main__":
    app.run(debug=True)
