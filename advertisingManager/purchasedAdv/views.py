from flask import redirect, render_template, url_for, Blueprint, request, abort
from flask_login import login_required
from advertisingManager.purchasedAdv.forms import AddPurchasedAdvForm, UpdatePurchasedAdvForm
from advertisingManager.models import User, Channel, PurchasedAdvertising
from advertisingManager import db
from flask_login import current_user
from sqlalchemy import func

purchasedAdv = Blueprint("purchasedAdv", __name__)

@purchasedAdv.route("/<int:channelID>/purchasedAdvs/add", methods=["GET", "POST"])
def add(channelID):
    form = AddPurchasedAdvForm()
    channel = db.session.get(Channel, channelID)
    userID = current_user.id
    
    
    if form.validate_on_submit():
        
        date = form.date.data
        channelLink = form.channelLink.data
        price = form.price.data
        
        purchasedAdv = PurchasedAdvertising(date, channelLink, price, channel.id, userID)
        db.session.add(purchasedAdv)
        db.session.commit()
        
        return redirect(url_for("purchasedAdv.purchasedAdvs", channelID = channel.id))
    
    return render_template("addPurchasedAdv.html", form = form, channelID = channel.id)


@purchasedAdv.route("/<int:channelID>/purchasedAdvs/<int:purchasedAdvID>/update", methods=["GET", "POST"])
def update(channelID, purchasedAdvID):
    form = UpdatePurchasedAdvForm()
    
    purchasedAdv = PurchasedAdvertising.query.get_or_404(purchasedAdvID)
    channelID = purchasedAdv.channelFID
    
    #if current_user.id != purchasedAdv.userFID:
    #    abort(403)
        
    if form.validate_on_submit():
        purchasedAdv.date = form.date.data
        purchasedAdv.channelLink = form.channelLink.data
        purchasedAdv.price = form.price.data
        purchasedAdv.numberOfNewSubs = form.numberOfNewSubs.data
        
        db.session.commit()
        return redirect(url_for("purchasedAdv.purchasedAdvs", channelID = channelID))
    
    elif request.method == 'GET':
        form.date.data = purchasedAdv.date
        form.channelLink.data = purchasedAdv.channelLink
        form.price.data = purchasedAdv.price
        form.numberOfNewSubs.data = purchasedAdv.numberOfNewSubs
    
    return render_template("updatePurchasedAdv.html", form = form, channelID = channelID)


@purchasedAdv.route("/<int:channelID>/purchasedAdvs/<int:purchasedAdvID>/delete")
def delete(channelID, purchasedAdvID):
    purchasedAdv = PurchasedAdvertising.query.get_or_404(purchasedAdvID)
    channelID = purchasedAdv.channelFID
    db.session.delete(purchasedAdv)
    db.session.commit()
    return redirect(url_for("purchasedAdv.purchasedAdvs", channelID = channelID))
    
    
    
@purchasedAdv.route("/<int:channelID>/purchasedAdvs")
def purchasedAdvs(channelID):
    purchasedAdvs = PurchasedAdvertising.query.filter_by(channelFID = channelID).order_by(PurchasedAdvertising.date.desc())
    
    totalPrice = db.session.query(func.sum(PurchasedAdvertising.price)).filter_by(channelFID = channelID).scalar()
    
    return render_template("purchasedAdvs.html", purchasedAdvs = purchasedAdvs, channelID = channelID, totalPrice = totalPrice)