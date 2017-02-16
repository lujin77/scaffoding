#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Blueprint, request, jsonify
from flask_restful import reqparse, Resource, inputs
from application.extensions import api
from application.core import log


api_bp = Blueprint('api', __name__, url_prefix='/api')
api.init_app(api_bp)


class TestAPI(Resource):
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('name', type=str, help=u'a string name', required=True)

    def get(self):
        args = self.parser.parse_args()
        self.name = args.get('name')
        log.info("flask_restful")
        return jsonify(result={"name": self.name})

api.add_resource(TestAPI, '/TestAPI', endpoint="api.TestAPI")
