from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateTimeField, DateField
from wtforms.validators import DataRequired

class AddSoldAdvForm(FlaskForm):
    date = DateField("Date", validators=[DataRequired()])
    channelLink = StringField("Channel link", validators=[DataRequired()])
    price = IntegerField("Price", validators=[DataRequired()])
    numberOfSubs = IntegerField("Number of subscribers", validators=[DataRequired()])
    submit = SubmitField("Add")
    

class UpdateSoldAdvForm(FlaskForm):
    date = DateField("Date")
    channelLink = StringField("Channel link")
    price = IntegerField("Price")
    numberOfSubs = IntegerField("Number of subscribers")
    submit = SubmitField("Update")