# Create your models here.
from sqlalchemy_utils import URLType
from app import db
from flask_login import UserMixin 
from datetime import datetime

#User's Model
''' User_ID, First_Name, Last_Name, Title, Area_Of_Study, School_Email'''

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default_user.jpg')
    #Add jpg
    #Hash to 20 characters
    password = db.Column(db.String(60), nullable=False)
    postexperiment = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class PostExperiment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    hypothesis_post = db.Column(db.Text, nullable=False)
    progress_post = db.Column(db.Integer, nullable=False)
    result_post = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"PostExperiment('{self.title}', '{self.date_posted}', '{self.hypothesis_post}', {self.progress_post}', '{self.result_post}')"

class PlantModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    formal_title  = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    plant_image = db.Column(db.String(20), nullable=False, default='default_plant.jpg')
    
    def __repr__(self):
        return f"PostExperiment('{self.title}', '{self.formal_title}', '{self.date_posted}', {self.plant_image}')"




#Plant's Model
'''Plant_ID, Common_Name, Latin_Name, Continent of Origin '''
#Experiment's Model
''' Experiment_ID, Time_Length, Hypothesis, Progress (number representing percentage), Field, '''
