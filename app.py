import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

title = "Flask with Databases"


@app.route('/')
def index():
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    return render_template('about.html', title=title)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('notfound.html', title=title, e=e)

if __name__ == '__main__':
    app.run(debug=True)
