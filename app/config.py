import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config:
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'Som3$ec5etK*y')
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', '').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
