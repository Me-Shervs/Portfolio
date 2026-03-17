from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50))
    degree = db.Column(db.String(128))

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(128))
    number = db.Column(db.String(20))
    subject = db.Column(db.String(128))
    message = db.Column(db.Text)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    github_link = db.Column(db.String(200))
    live_demo = db.Column(db.String(200))
    image_filename = db.Column(db.String(100)) # !important this store name of the image file

class Certificate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    pdf_filename = db.Column(db.String(100))
    image_filename = db.Column(db.String(100))
