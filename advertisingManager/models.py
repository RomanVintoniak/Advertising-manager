from advertisingManager import db, loginManager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

@loginManager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True, index = True)
    email = db.Column(db.String(64), unique = True, index = True)
    passwordHash = db.Column(db.String(128))
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.passwordHash = generate_password_hash(password)
        
    def __repr__(self):
        return f"email: {self.email}"
    
    def checkPassword(self, password):
        return check_password_hash(self.passwordHash, password)
    


class Channel(db.Model):
    __tablename__ = "channels"
    
    id = db.Column(db.Integer, primary_key = True)
    logo = db.Column(db.String(64), nullable = False, default = 'defaultLogo.png')
    name = db.Column(db.String(64), nullable = False)
    userFID = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    
    purchasedAdvertisings = db.relationship('PurchasedAdvertising', backref = 'channel', lazy = True)
    soldAdvertisings = db.relationship('SoldAdvertising', backref = 'channel', lazy = True)
    
    def __init__(self, name, userFID):
        self.name = name
        self.userFID = userFID
    
    

class PurchasedAdvertising(db.Model):
    __tablename__ = "purchasedAdvertisings"
    
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime, nullable = False, default = datetime.now) 
    channelLink = db.Column(db.String(128), nullable = False)
    price = db.Column(db.Integer)
    numberOfNewSubs = db.Column(db.Integer, default = 0)
    channelFID = db.Column(db.Integer, db.ForeignKey('channels.id'), nullable = False)
    userFID = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    
    def __init__(self, date, channelLink, price, channelFID, userFID):
        self.date = date
        self.channelLink = channelLink
        self.price = price
        self.channelFID = channelFID
        self.userFID = userFID



class SoldAdvertising(db.Model):
    __tablename__ = "soldAdvertisings"
    
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime, nullable = False, default = datetime.now)
    channelLink = db.Column(db.String(128), nullable = False)
    price = db.Column(db.Integer)
    numberOfSubs = db.Column(db.Integer)
    channelFID = db.Column(db.Integer, db.ForeignKey('channels.id'), nullable = False)
    userFID = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    
    def __init__(self, date, channelLink, price, numberOfSubs, channelFID, userFID):
        self.date = date
        self.channelLink = channelLink
        self.price = price
        self.numberOfSubs = numberOfSubs
        self.channelFID = channelFID
        self.userFID = userFID