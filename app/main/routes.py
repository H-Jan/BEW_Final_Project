from flask import Blueprint
from flask import Flask, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db


#app = Flask(__name__)

#app.config['SECRET KEY'] = '1122334455667788'

main = Blueprint('main', __name__)

from .forms import RegistrationForm, LoginForm

# Create your routes here.
'''Login Page - Displays the login requirements

Current Experiments Page - Display's all active, ongoing experiments, allows User to determine when completed 

Completed Experiments Page - Display's all completed experiments

Particular Experiment Page - Display's the information of a particular experiment including its purpose, hypothesis, and result 

Plants In Stock - Display's all plants that are currently available for experimentation

Past Plant's Used - Display's all previous plants used for experimentation

Plant Details - Display's the details of a particular plant 
'''

geninfo = [
    {
        'professor' : 'Hani Jandali',
        'Experiment_Title' : 'Cassava Plants Immunity',
        'hypothesis' : 'Cassava is inherently immune',
        'Progress': '50%'
    },
    {
        'professor' : 'Miranda L',
        'Experiment_Title' : 'Healthy Lettuce ',
        'hypothesis' : 'Its Yummu',
        'Progress': '30%'
    },
]

@app.route("/")
def general():
    return render_template('home.html', geninfo = geninfo)

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
    #The form=form is going back to form=RegistrationForm()

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login is unsuccessful. Please check in username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/about")
def about():
    return 