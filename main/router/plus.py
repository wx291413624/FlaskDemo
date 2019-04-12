# coding=utf-8
from flask_restplus import Resource

from main import api

ns = api.namespace('management', description='A simple Back-stage management API')


@ns.route('/login')
class HelloWorld(Resource):
    @ns.param('id', 'The task identifier')
    def get(self):
        return {'hello': 'world'}

    @ns.param('ids', 'The task identifier')
    def put(self):
        return {'hello': 'world'}
