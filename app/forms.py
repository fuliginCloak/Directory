from flask_wtf import  FlaskForm
from wtforms import StringField, SubmitField, TextField, DateField, FloatField, IntegerField, MultipleFileField, SelectField
from flask_wtf.file import  FileAllowed
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


class AddListing(FlaskForm):
    title = StringField('Listing Title', validators=[DataRequired()])
    price = IntegerField("Asking Price", validators = [DataRequired()])
    acres = FloatField('Total Acres', validators = [DataRequired()])

    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]    
    

    state = SelectField('What State', choices=states, validators=[DataRequired()])
    county = StringField('What County',  validators=[DataRequired()])
    city = StringField('What City',  validators=[DataRequired()])


    images = MultipleFileField('Select Image(s)', validators = [DataRequired(), FileAllowed(['jpg','png'])])
    upload = SubmitField('Upload Images')
    short = TextField('Provide Summary of Description', validators = [DataRequired(), Length(2,120)])
    long = TextField('Provide Full Description', validators = [DataRequired()])