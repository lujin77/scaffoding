# coding: utf-8
import os

from .default import Config


class DevelopmentConfig(Config):
    """Base config class."""
    # Flask app config
    DEBUG = True
    TESTING = False
    SECRET_KEY = "sample_key"

    # SQLAlchemy config
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

    # MongoEngine config
    '''
    MONGODB_SETTINGS = {
        'db': 'your_db',
        'host': 'localhost',
        'port': 27017
    }
    '''
