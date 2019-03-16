import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) #Creates a db object

##############################################################################

class Puppy(db.Model):
    __tablename__ = 'puppies'  # This overides the default table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    fur = db.Column(db.Text)
    sex = db.Column(db.Text)

    def __init__(self,name,age): #initiates the object
        self.name = name
        self.age = age

    def __repr__(self): #Provides a string representation of the object
        return f"Puppy with a name of {self.name} is {self.age} year(s) old. His/Her fur color is: {self.color}."

title = "Flask with Databases"

@app.route('/')
def index():
    return render_template('index.html', title=title, basedir=basedir)

@app.route('/about')
def about():
    return render_template('about.html', title=title)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('notfound.html', title=title, e=e)

if __name__ == '__main__':
    app.run(debug=True)
