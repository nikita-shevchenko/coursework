from flask import Blueprint, render_template
from app import db
from forms import AuthForm

main = Blueprint('main', __name__)


@main.route('/')
def hello_world():
    auth_form = AuthForm()
    return render_template('main.html', form=auth_form)


@main.route('/dashboard')
def dashboard():
    return 'restricted'