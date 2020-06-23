from app import app, db
from app.forms import  PaymentForm , AddPost, LoginForm, RegisterForm
from flask import render_template, send_file, redirect, url_for, flash, request
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User, Listing
from datetime import datetime




@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/payments')
def processing():
    form = PaymentForm()
    return render_template('processing.html', title ='Payment', form=form)


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    
    return render_template('register.html', title ='Register', form=form)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('post'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Power User', form=form)
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/land-listing', methods=['GET', 'POST'])
@login_required
def post() :
    form = AddPost()
    form.set_context()
    
    
    print(form.errors)
    
    if form.is_submitted():
        print ("submitted")

    if form.validate():
        print ("valid")

    print(form.errors)

   
    if form.validate_on_submit():
        new_listing = Listing(
            db_title=form.title.data,
            db_state=form.state.data,
            db_county=form.county.data,
            db_acres=form.acres.data,
            db_short=form.short.data,
            db_long=form.long.data,
            timestamp=datetime.now()
        )
    
        db.session.add(new_listing)
        db.session.commit()
        print('Land added to database')
    

    # db_images = url_for('static', filename='showcase/')
    return render_template('posts.html', title = "Land for sale", form=form)



@app.route('/land')
def parcel():
    return render_template('parcels.html', title = 'Land for Sale')

@app.route('/about')
def about():
    return render_template('about.html', title = "About")

@app.route('/faq')
def faq():
    return render_template('faq.html', title = 'FAQ')