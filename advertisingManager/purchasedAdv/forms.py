from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateTimeField, DateField
from wtforms.validators import DataRequired

class AddPurchasedAdvForm(FlaskForm):
    date = DateField("Data", validators=[DataRequired()])
    channelLink = StringField("Channel link", validators=[DataRequired()])
    price = IntegerField("Price", validators=[DataRequired()])
    submit = SubmitField("Add")
    
class UpdatePurchasedAdvForm(FlaskForm):
    date = DateField("Data")
    channelLink = StringField("Channel link")
    price = IntegerField("Price")
    numberOfNewSubs = IntegerField("Number of new subscribers")
    submit = SubmitField("Update")