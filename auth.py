from flask import Blueprint, request, flash, url_for, redirect
from app import db
from models import Student
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    student = Student.query.filter_by(student_email=email).first()

    if not student or not check_password_hash(password, student.student_password):
        flash('Please check your login details and try again.')
        return redirect(url_for('main.dashboard'))

    return 'login'


@auth.route('/logout')
def logout():
    return 'logout'
