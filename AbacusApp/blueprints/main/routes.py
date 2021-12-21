from flask import Blueprint
from flask.templating import render_template

main = Blueprint('main', __name__)

@main.route("/", methods=['GET', 'POST'])
def sign_in():
    return render_template('base_template.html')