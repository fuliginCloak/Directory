from app import app
from app.forms import  PaymentForm 
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/payments')
def processing():
    form = PaymentForm()
    return render_template('processing.html', title ='Payment', form=form)

@app.route('/land-listings')
def listings():
    return render_template('listings.html', title = "Land for sale")

@app.route('/about')
def about():
    return render_template('about.html', title = "About")