# Add any model classes for Flask-SQLAlchemy here
from datetime import datetime
from . import db

class Movie(db.Model):
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    poster_url = db.Column(db.String(200))
    release_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    def __init__(self, title, description=None, poster_url=None, release_date=None):
        self.title = title
        self.description = description
        self.poster_url = poster_url
        self.release_date = release_date

    def __repr__(self):
        return f"<Movie {self.id}: {self.title}>"
