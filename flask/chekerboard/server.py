
from os import times
from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/') #@app.route('/repeat/<int:num>/<name>')
def first():
    title = "CheckerBoard"
    return render_template('index.html', title_from_backend = title)  # Return the string 'Hello World!' as a response
    

@app.route('/play/<int:i>/<int:j>') #@app.route('/repeat/<int:num>/<name>')
def play(i, j):
    title = "CheckerBoard"
    print(i, j)
    return render_template('index.html', i = i, title_from_backend = title, j=j)  # Return the string 'Hello World!' as a response



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
