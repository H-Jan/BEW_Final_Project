# Create your forms here.
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, PasswordField, FloatField, BooleanField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, URL, ValidationError, Email, EqualTo, ValidationError
from app.models import User, PostExperiment, PlantModel

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    #Used as our label in html 
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    #BE SURE TO INCLUDE NEXXT TO USERNAME IN HTML
    profession = StringField('Profession', validators=[DataRequired(), Length(min=1, max=30)])
    #Run Test for equals between password and confirm password
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Unfortunately this username is already taken, please choose another one')
    
    #For unique fields

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('Unfortunately this email is already taken, please choose another one')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    #Used as our label in html 
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    #Run Test for equals between password and confirm password
    submit = SubmitField('Login')

class ExperimentForm(FlaskForm):
    """Form for adding/updating an Ongoing Experiment"""
    title = StringField('Experiment', validators=[DataRequired(), Length(min=1, max=30)])
    hypothesis = StringField('Hypothesis', validators=[DataRequired(), Length(min=1, max=300)])
    progress = StringField('Progress', validators=[DataRequired()])
    result = StringField('Result', validators=[DataRequired()])
    exp_photo = StringField('Experiment Photo', validators=[URL()])
    submit = SubmitField('Save')

class PlantForm(FlaskForm):
    """Form for adding/updating a Plant and its information"""
    normal_name = StringField('Normal Name', validators=[DataRequired()])
    scientific_name = StringField('Science Name', validators=[DataRequired()])
    plant_photo = StringField('Plant Photo', validators=[URL()])
    submit = SubmitField('Save')


class AccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

