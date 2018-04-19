from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators, ValidationError

class QRForm(Form):
    texts = TextField("Enter medicine name", [validators.Required("Please enter medicine name!!!")])
    submit = SubmitField("GO")
