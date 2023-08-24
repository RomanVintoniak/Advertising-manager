from advertisingManager import db
from advertisingManager.models import User, Channel, PurchasedAdvertising, SoldAdvertising
from sqlalchemy import func
from datetime import datetime

#user1 = db.session.get(User, 1)
#user2 = db.session.get(User, 2)
#print(user1.passwordHash)
#print(user2.passwordHash)

#channels = Channel.query.filter_by(userFID = 1).all()
#for channel in channels:
#    print(channel.name)

#channel = db.session.get(Channel, 4)
#purchasedAdvertisings = channel.purchasedAdvertisings
#for adv in purchasedAdvertisings:
#    print(adv.channelLink)

#test = db.session.query(func.sum(PurchasedAdvertising.price)).filter_by(channelFID = 4).scalar()
#print(test)

#date = datetime.now().strftime("%d.%m.%Y")
#print(date)

#adv = db.session.query(PurchasedAdvertising).all()
#print(adv)

#adv = db.session.get(PurchasedAdvertising, 1)

#test