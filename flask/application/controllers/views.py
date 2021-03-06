#!/usr/bin/env python
# encoding: utf-8
import json

from flask import Blueprint, request, jsonify
from application.core import log


view_bp = Blueprint('view', __name__)

@view_bp.route('/', methods=['GET'])
def index():
    log.info("welcome")
    return jsonify({'info': 'welcome'})

@view_bp.route('/get', methods=['GET'])
def get():
    name = request.args.get('name')
    log.info(name)
    return jsonify({'name': name})

@view_bp.route('/post', methods=['POST'])
def post():
    data = json.loads(request.data)
    log.info(request.data)
    return jsonify({'data': data})
