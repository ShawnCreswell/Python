from flask import Flask, render_template  
app = Flask(__name__)   


@app.route('/') #@app.route('/repeat/<int:num>/<name>')
def first():
    title = "CheckerBoard"
    return render_template('index.html', title_from_backend = title)  # Return the string 'Hello World!' as a response
    




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
