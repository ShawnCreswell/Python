from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "money"

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    session['strawberry'] = request.form['strawberry']
    session['raspberry'] = request.form['raspberry']
    session['apple'] = request.form['apple']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']

    print("Charging", request.form['first_name'], request.form['last_name'], "for", int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple']), "fruits" )


    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")
    
    
if __name__=="__main__":   
    app.run(debug=True)    