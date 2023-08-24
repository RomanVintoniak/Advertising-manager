from flask import abort, redirect, render_template, url_for, request, Blueprint
from flask_login import current_user, login_required
from advertisingManager.channels.logoHandler import addChannelLogo
from advertisingManager.channels.forms import AddChannelForm, UpdateChannelForm
from advertisingManager.models import Channel
from advertisingManager import db
import sys

channels = Blueprint("channels", __name__)


@channels.route("/addChannel", methods=["GET", "POST"])
def add():
    form = AddChannelForm()
    
    if form.validate_on_submit():
        name = form.name.data
        userID = current_user.id
        
        channel = Channel(name, userID)
        
        db.session.add(channel)
        db.session.commit()
        
        return redirect(url_for("users.channels", userID = userID))
    
    return render_template("addChannel.html", form = form)


@channels.route("/<int:channelID>/updateChannel", methods=["GET", "POST"])
@login_required
def update(channelID):
    channel = Channel.query.get_or_404(channelID)
    
    if current_user.id != channel.userFID:
        abort(403)
    
    form = UpdateChannelForm()
    
    if form.validate_on_submit():
        if form.logo.data:
            channelName = channel.name
            newLogo = addChannelLogo(form.logo.data, channelName)
            channel.logo = newLogo
        
        channel.name = form.name.data
        db.session.commit()
        return redirect(url_for('users.channels', userID = current_user.id))
    
    elif request.method == 'GET':
        form.name.data = channel.name
    
    logo = url_for('static', filename='channelsLogo/' + channel.logo)
    return render_template('updateChannel.html', form = form, logo = logo)
    

@channels.route("/<int:channelID>/delete", methods = ["GET", "POST"])
@login_required
def delete(channelID):
    channel = Channel.query.get_or_404(channelID)

    if channel.userFID != current_user.id:
        abort(403)
    
    db.session.delete(channel)
    db.session.commit()
    return redirect(url_for("users.channels", userID = current_user.id))

