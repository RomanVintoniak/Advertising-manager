from flask import render_template, url_for, Blueprint
from flask_login import current_user
from advertisingManager.models import Channel
from advertisingManager import db

core = Blueprint('core', __name__)

@core.route("/")
def index():
    #channels = Channel.query.filter_by(userFID = current_user.id).all()
    return render_template("index.html")