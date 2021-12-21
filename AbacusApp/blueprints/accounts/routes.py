from flask import Blueprint
from flask.templating import render_template

accounts = Blueprint('account', __name__)

@accounts.route("/sign-in", methods=['GET', 'POST'])
def sign_in():
    return render_template('signin.html')

@accounts.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    return render_template('signup.html')