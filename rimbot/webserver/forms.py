from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username    = StringField('User', validators=[DataRequired("Please, enter a valid username!")])
    password    = PasswordField('Password', validators=[DataRequired("Please, enter a valid password!")])
    remember_me = BooleanField('Remember me')
    submit      = SubmitField('Sign In')