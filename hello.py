from flask import Flask, render_template


# Create a flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
# def index():
#     return "<h1>Hello world!</h1>"

def index():
    firstname = "John"
    stuff = "This is <strong>Bold</strong> Text"
    favorites_pizza = ['Pepperoni', 'Cheese', 'Mushrooms', 41]
    return render_template('index.html', firstname = firstname, stuff=stuff, favorites_pizza = favorites_pizza)






@app.route('/user/<name>')
def user(name):
    return render_template('user.html', username=name)


# Create Custom Error Pages
@app.errorhandler(404)
def page_not_found(e):
     return render_template('404.html'), 404

# Internal Server Error 
@app.errorhandler(500)
def page_not_found(e):
     return render_template('500.html'), 500











app.run(debug=True)

