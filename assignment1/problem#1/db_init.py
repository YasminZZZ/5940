from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/workshop'
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.db'
app.config['SECRET_KEY'] = "mysecret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(255))
    post_date = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    # postdate = db.Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return '<Blog %r>' % self.id
    
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(255))
    password = db.Column(db.String(80))
    bio = db.Column(db.Text, nullable=False)
    admin = db.Column(db.Boolean)
    image_file = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    
    
    def __repr__(self):
        return '<User %r>' % self.id