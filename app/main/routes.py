from flask import Blueprint
from flask import Flask, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from flask_bcrypt import Bcrypt

main = Blueprint('main', __name__)

from .forms import RegistrationForm, LoginForm, ExperimentForm, PlantForm
from app.models import User, PostExperiment
bcrypt = Bcrypt(app)

# Create your routes here.
'''Login Page - Displays the login requirements

Current Experiments Page - Display's all active, ongoing experiments, allows User to determine when completed 

Completed Experiments Page - Display's all completed experiments

Particular Experiment Page - Display's the information of a particular experiment including its purpose, hypothesis, and result 

Plants In Stock - Display's all plants that are currently available for experimentation

Past Plant's Used - Display's all previous plants used for experimentation

Plant Details - Display's the details of a particular plant 
'''


@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created, you can now log in', 'success')
        return redirect(url_for('login'))
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