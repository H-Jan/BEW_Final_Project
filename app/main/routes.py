from flask import Blueprint
from flask import Flask, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db, Bcrypt

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

#New Register is the immediate route
@app.route("/", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created, you can now log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
    #The form=form is going back to form=RegistrationForm()

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            #next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)


@app.route("/experiment/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = ExperimentForm()
    if form.validate_on_submit():
        post = PostExperiment(title=form.title.data, hypothesis_post= form.hypothesis.data, progress_post = form.progress.data, results = form.result.data)
        db.session.add(post)
        db.session.commit()
        flash('Your Experiment has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('experiments.html', title='New Experiment',
                           form=form)


@app.route("/plant/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PlantForm()
    if form.validate_on_submit():
        post = PlantModel(normal_name=form.normal_name.data, scientific_name=form.scientific_name.data)
        db.session.add(post)
        db.session.commit()
        flash('Your Plant has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('plants.html', title='New Plant',
                           form=form)


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = AccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)

@app.route("/about")
def about():
    return 