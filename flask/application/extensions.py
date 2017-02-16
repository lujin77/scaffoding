#!/usr/bin/env python
# encoding: utf-8
from flask_restful import Api
from flask_redis import FlaskRedis
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy


api = Api()
redis = FlaskRedis()
mongo = PyMongo()
db = SQLAlchemy()
