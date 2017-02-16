# coding: utf-8
import os

from .default import Config


class TestingConfig(Config):
    # Flask app config
    DEBUG = False
    TESTING = True
    SECRET_KEY = "sample_key"

    # MongoEngine config
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@localhost/flask"
