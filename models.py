from app import db
from flask_login import UserMixin


class Student(UserMixin, db.Model):
    record_book = db.Column(db.String(6), primary_key=True)
    group_year = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(10), nullable=False)
    student_name = db.Column(db.String(500), nullable=False)
    student_email = db.Column(db.String(200), nullable=False, unique=True)
    student_password = db.Column(db.String(64), nullable=False)
    student_phone = db.Column(db.String(50), nullable=True)
