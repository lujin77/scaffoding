#!/usr/bin/env python
# encoding: utf-8
from application.extensions import db

__all__ = ['User']


class User(db.Model):
    __table__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
