from flask import Blueprint
from flask import render_template


main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('index.html')

@main.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")