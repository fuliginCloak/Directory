from flask_wtf import  FlaskForm
from wtforms import StringField, SubmitField, DateField, FloatField, IntegerField
from wtforms.validators import DataRequired, Email, Length



class PaymentForm(FlaskForm):
    fullname = StringField('Full Name', validators = [DataRequired()])
    email = StringField('Email Address', validators = [DataRequired(),Email()])
    card_number = IntegerField('Credit Card Number', validators = [DataRequired(), Length(16,16)])
    exp_date = DateField('Exp Date', validators = [DataRequired(), Length(3,3)])
    security = IntegerField('Security Code', validators = [DataRequired()])
    zip_code = IntegerField('Billing Zip Code', validators = [DataRequired()])
    amount = FloatField ('Payment Amount', validators = [DataRequired()])
    submit = SubmitField('Submit Payment')