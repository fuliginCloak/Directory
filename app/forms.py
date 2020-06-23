from flask_wtf import  FlaskForm
from wtforms import StringField, BooleanField, SubmitField, TextField, DateField, FloatField, IntegerField, MultipleFileField, SelectField
from flask_wtf.file import  FileAllowed
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from app.models import User



class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = StringField('password',  validators = [DataRequired()])
    remember = BooleanField("save username?")
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Choose username', validators = [DataRequired()])
    password = StringField('Choose password',  validators = [Length(6,24), DataRequired()])
    # confirm = StringField('Confirm password', validators = [DataRequired(), EqualTo(password)])
    submit = SubmitField('Make account')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')



class PaymentForm(FlaskForm):
    fullname = StringField('Full Name', validators = [DataRequired()])
    email = StringField('Email Address', validators = [DataRequired(),Email()])
    card_number = IntegerField('Credit Card Number', validators = [DataRequired(), Length(16,16)])
    exp_date = DateField('Exp Date', validators = [DataRequired(), Length(3,3)])
    security = IntegerField('Security Code', validators = [DataRequired()])
    zip_code = IntegerField('Billing Zip Code', validators = [DataRequired()])
    amount = FloatField ('Payment Amount', validators = [DataRequired()])
    submit = SubmitField('Submit Payment')


class AddPost(FlaskForm):
    title = StringField('Listing Title', validators=[DataRequired()])
    price = StringField('Asking Price', validators=[DataRequired()])
    acres = FloatField('Total Acres') 
    

    state = SelectField('What State', coerce=str, validators=[DataRequired()])
    county = StringField('What County')


   
    short = TextField('Provide Summary of Description', validators=[DataRequired()])
    long = TextField('Provide Full Description')
    images = MultipleFileField('Select Images', validators = [FileAllowed(['jpg','png', 'jpeg'])])
    

    submit = SubmitField('Submit listing')

    def set_context(self):
        self.state.choices = [("AL", "AL"), ("AK","AK"), ("AZ","AZ"), ("AR","AR"), ("CA","CA"), ("CO","CO"), ("CT","CT"), ("DC","DC"),("DE","DE"), ("FL","FL"), 
          ("GA","GA"), ("HI","HI"), ("ID","ID"), ("IL", "IL"), ("IN","IN"), ("IA","IA"), ("KS","KS"), ("KY","KY"), ("LA","LA"),("MA","MA"), ("MD","MD"), ("ME","ME"), 
          ("MI","MI"), ("MN","MN"), ("MS","MS"), ("MO", "MO"), ("MT","MT"), ("NC","NC"), ("ND", "ND"), ("NE","NE"), ("NH","NH"), ("NJ","NJ"), ("NV","NV"), 
          ("NM","NM"), ("NY","NY"), ("OH","OH"), ("OK","OK"),("OR","OR") , ("PA","PA"), ("RI","RI"), ( "SC", "SC"), 
          ("SD","SD"), ("TN","TN"), ("TX","TX"), ("UT","UT"), ("VA","VA"), ("VT","VT"),  ("WA","WA"), ("WI","WI"), ("WV","WV"), ("WY","WY")]   

  
         