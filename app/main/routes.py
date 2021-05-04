from flask import Blueprint
from flask import Flask, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db

main = Blueprint('main', __name__)

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

@app.route("/about")
def about():
    return 