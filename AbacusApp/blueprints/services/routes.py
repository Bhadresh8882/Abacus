from flask import Blueprint
from flask.templating import render_template

services = Blueprint('services', __name__)

@services.route("/video", methods=['GET', 'POST'])
def sign_in():
    return render_template('video.html')