from app import app
from app.forms import  PaymentForm , AddListing
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
    form = AddListing()
    return render_template('listings.html', title = "Land for sale", form=form)

@app.route('/about')
def about():
    return render_template('about.html', title = "About")

@app.route('/faq')
def faq():
    return render_template('faq.html', title = 'FAQ')