from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    remember_me=BooleanField('Remember Me')
    submit=SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    password2=PasswordField('Repeat Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Register')

    def validate_username(self,username): #custom validator
        user=User.query.filter_by(username=username.data).first() #tablename.query.filter_by(similar to where condition)
        if user is not None:
            raise ValidationError("plesae use a different username")

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first() #query to stop as soon as it finds one matching result and return it
        if user is not None:
            raise ValidationError("please use a different email address")