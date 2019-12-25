from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField
from wtforms.validators import Email, regexp, Length


class AuthForm(FlaskForm):
    email = StringField('email', validators=[Email()])
    password = StringField('password', validators=[Length(6, 20)])
