# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Shambhvi Dixit"
    age = "13" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father we
app.route("./mother")
def home():

    name = "Prachi Dixit"
     # write your age

    return render_template('mother.html' , name = name )

# define the route to mother webpage
app.route("./father")
def home():

    name = "Sudhir Dixit"
     # write your age

    return render_template('father.html' , name = name )

# define the route to friends webpage
app.route("./friend")
def home():

    name = "Prachi Dixit"
     # write your age

    return render_template('friend.html' , name = name )

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
