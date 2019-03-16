from flask import Flask, render_template
app = Flask(__name__)

title = "Flask with Databases"


@app.route('/')
def index():
    return render_template('index.html', title=title)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('notfound.html', title=title, e=e)

if __name__ == '__main__':
    app.run(debug=True)
