from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import requests
import os

RAVELRY_USERNAME=os.getenv('RAVELRY_USERNAME')
RAVELRY_PASSWORD=os.getenv('RAVELRY_PASSWORD')
DEBUG=os.getenv('DEBUG', 'True') == 'True'

app = Flask(__name__)
api = Api(app)

class Index(Resource):
    def get(self):
        return "Wrapper for Ravlery API"

class Users(Resource):
    def get(self, name):
        res = requests.get('https://api.ravelry.com/people/{}.json'.format(name), auth=requests.auth.HTTPBasicAuth(RAVELRY_USERNAME, RAVELRY_PASSWORD))
        return res.json()

class Patterns(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('pc', type=str)
        parser.add_argument('weight', type=str)
        parser.add_argument('view', type=str)
        parser.add_argument('sort', type=str)
        parser.add_argument('fit', type=str)
        parser.add_argument('craft', type=str)
        parser.add_argument('colors', type=int, help='Colors must be an integer')
        args = parser.parse_args()

        pc = args['pc']
        weight = args['weight']
        view = args['view']
        sort = args['sort']
        fit = args['fit']
        craft = args['craft']
        colors = args['colors']
        res = requests.get('https://api.ravelry.com/patterns/search.json?pc={}&weight={}&view={}&sort={}&fit={}&craft={}&colors={}'.format(pc, weight, view, sort, fit, craft, colors), auth=requests.auth.HTTPBasicAuth(RAVELRY_USERNAME, RAVELRY_PASSWORD))

        return res.json()

api.add_resource(Index, '/')
api.add_resource(Users, '/users/<string:name>')
api.add_resource(Patterns, '/patterns')

if __name__ == '__main__':
    app.run(debug=DEBUG)
