from turtle import title
from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/play')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    title = "Checker Board"
    return render_template('index.html', title_from_backend = title)  # Return the string 'Hello World!' as a response


@app.route('/play/<int:num>') #@app.route('/repeat/<int:num>/<name>')
def play(num):
    # return f"hello { * (num)}"
    title = "Welcome!"
    return render_template('index.html', num = num, title_from_backend = title)  # Return the string 'Hello World!' as a response
    

@app.route('/play/<int:num>/<string:color>') #@app.route('/repeat/<int:num>/<name>')
def color(num, color):
    title = "Welcome!"
    return render_template('index.html', num = num, title_from_backend = title, color = color)  # Return the string 'Hello World!' as a response
    



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
