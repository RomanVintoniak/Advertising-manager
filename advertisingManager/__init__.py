import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db = SQLAlchemy(app)
Migrate(app, db)

loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = 'users.login'

from advertisingManager.core.views import core
from advertisingManager.users.views import users
from advertisingManager.channels.views import channels
from advertisingManager.purchasedAdv.views import purchasedAdv
from advertisingManager.soldAdv.views import soldAdv

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(channels)
app.register_blueprint(purchasedAdv)
app.register_blueprint(soldAdv)