from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    movies = db.relationship('Movie', backref='user', lazy=True, cascade="all, delete-orphan")

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    director = db.Column(db.String(100))
    year = db.Column(db.String(4))
    poster_url = db.Column(db.String(512))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
