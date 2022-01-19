from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 64)])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Keep me logged in')
  submit = SubmitField('Log In')
