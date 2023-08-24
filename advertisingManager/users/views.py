from flask import redirect, render_template, url_for, Blueprint, request
from flask_login import login_user, logout_user, login_required
from advertisingManager.users.forms import RegistrationForm, LoginForm
from advertisingManager.models import User, Channel
from advertisingManager import db
from flask_login import current_user

users = Blueprint("users", __name__)

@users.route("/registration", methods = ["GET", "POST"])
def registration():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        
        user = User(username, email, password)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for("users.login"))
    
    return render_template("regisration.html", form = form)


@users.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():

        user = User.query.filter_by(email = form.email.data).first()

        if user.checkPassword(form.password.data) and user is not None:

            login_user(user)

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('users.channels', userID = current_user.id)

            return redirect(next)

    return render_template('login.html', form = form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core.index"))


@users.route("/<int:userID>/channels")
def channels(userID):
    channels = Channel.query.filter_by(userFID = userID).all()
    return render_template("channels.html", channels = channels)