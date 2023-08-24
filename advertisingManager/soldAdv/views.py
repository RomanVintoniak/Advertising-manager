from flask import redirect, render_template, url_for, Blueprint, request, abort
from flask_login import login_required
from advertisingManager.soldAdv.forms import AddSoldAdvForm, UpdateSoldAdvForm
from advertisingManager.models import User, Channel, SoldAdvertising
from advertisingManager import db
from flask_login import current_user
from sqlalchemy import func

soldAdv = Blueprint("soldAdv", __name__)

@soldAdv.route("/<int:channelID>/soldAdvs/add", methods=["GET", "POST"])
def add(channelID):
    form = AddSoldAdvForm()
    userID = current_user.id
    
    if form.validate_on_submit():
        date = form.date.data
        channelLink = form.channelLink.data
        price = form.price.data
        numberOfSubs = form.numberOfSubs.data
        
        soldAdv = SoldAdvertising(date, channelLink, price, numberOfSubs, channelID, userID)
        
        db.session.add(soldAdv)
        db.session.commit()
        
        return redirect(url_for("soldAdv.soldAdvs", channelID = channelID))
    
    return render_template("addSoldAdv.html", form = form, channelID = channelID)


@soldAdv.route("/<int:channelID>/soldAdvs/<int:soldAdvID>/update", methods=["GET", "POST"])
def update(channelID, soldAdvID):
    soldAdv = SoldAdvertising.query.get_or_404(soldAdvID)
    form = UpdateSoldAdvForm()

    if form.validate_on_submit():
        soldAdv.date = form.date.data
        soldAdv.channelLink = form.channelLink.data
        soldAdv.price = form.price.data
        soldAdv.numberOfSubs = form.numberOfSubs.data
        
        db.session.commit()
        return redirect(url_for("soldAdv.soldAdvs", channelID = channelID))
    
    elif request.method == "GET":
        form.date.data = soldAdv.date
        form.channelLink.data = soldAdv.channelLink
        form.price.data = soldAdv.price
        form.numberOfSubs.data = soldAdv.numberOfSubs
    
    return render_template("updateSoldAdv.html", form = form, channelID = channelID)


@soldAdv.route("/<int:channelID>/soldAdvs/<int:soldAdvID>/delete")
def delete(channelID, soldAdvID):
    soldAdv = SoldAdvertising.query.get_or_404(soldAdvID)
    db.session.delete(soldAdv)
    db.session.commit()
    return redirect(url_for("soldAdv.soldAdvs", channelID = channelID))


@soldAdv.route("/<int:channelID>/soldAdvs")
def soldAdvs(channelID):
    soldAdvs = SoldAdvertising.query.filter_by(channelFID = channelID).order_by(SoldAdvertising.date.desc())
    
    totalPrice = db.session.query(func.sum(SoldAdvertising.price)).filter_by(channelFID = channelID).scalar()
    
    return render_template("soldAdvs.html", soldAdvs = soldAdvs, channelID = channelID, totalPrice = totalPrice)
        