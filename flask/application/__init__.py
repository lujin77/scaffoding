#!/usr/bin/env python
# encoding: utf-8
import os
import sys

from flask import Flask, current_app

from config import load_config
from application.extensions import api, redis, mongo, db
from application.controllers import all_bp

# convert python's encoding to utf8
try:
    reload(sys)
    sys.setdefaultencoding('utf8')
except (AttributeError, NameError):
    pass


def create_app(mode):
    """Create Flask app."""
    config = load_config(mode)

    app = Flask(__name__)
    app.config.from_object(config)

    if not hasattr(app, 'production'):
        app.production = not app.debug and not app.testing

    # Register components
    configure_logging(app)
    register_extensions(app)
    register_blueprint(app)

    app.logger.info("flask app create complete!")

    return app


def register_extensions(app):
    """Register models."""
    db.init_app(app)
    with app.app_context():
        db.create_all()
    redis.init_app(app)
    mongo.init_app(app)


def register_blueprint(app):
    for bp in all_bp:
        app.register_blueprint(bp)


def configure_logging(app):

    import logging
    from logging import Formatter
    from logging.handlers import RotatingFileHandler

    FORMAT = "%(asctime)-15s %(levelname)s - %(message)s"
    FORMAT_ERR = "%(asctime)s %(levelname)s - %(message)s [in %(pathname)s:%(lineno)d - %(funcName)s]"

    logging.basicConfig(format=FORMAT)
    if app.config.get('TESTING'):
        app.logger.setLevel(logging.CRITICAL)
        return
    elif app.config.get('DEBUG'):
        app.logger.setLevel(logging.DEBUG)
        return

    app.logger.setLevel(logging.INFO)

    # info log
    path = os.path.join(app.config['PROJECT_PATH'], "log/{}_info.log".format(app.config['SITE_TITLE']))
    info_file_handler = RotatingFileHandler(path, maxBytes=104857600, backupCount=10)
    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(Formatter(FORMAT))
    app.logger.addHandler(info_file_handler)
    # error log
    path = os.path.join(app.config['PROJECT_PATH'], "log/{}_err.log".format(app.config['SITE_TITLE']))
    err_file_handler = RotatingFileHandler(path, maxBytes=104857600, backupCount=10)
    err_file_handler.setLevel(logging.ERROR)
    err_file_handler.setFormatter(Formatter(FORMAT_ERR))
    app.logger.addHandler(err_file_handler)