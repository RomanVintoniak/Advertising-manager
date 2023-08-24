from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired

class AddChannelForm(FlaskForm):
    name = StringField("Channel name",validators=[DataRequired()])
    submit = SubmitField("Add")
    

class UpdateChannelForm(FlaskForm):
    name = StringField("Channel name")
    logo = FileField('Update channel logo', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Update")