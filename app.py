from flask import Flask
from flask import jsonify
from flask import request
import requests
import os

RAVELRY_USERNAME=os.getenv('RAVELRY_USERNAME')
RAVELRY_PASSWORD=os.getenv('RAVELRY_PASSWORD')

app = Flask(__name__)

@app.route('/')
def index():
    return "Wrapper for Ravlery API"

@app.route('/users/<name>')
def users(name=''):
    res = requests.get('https://api.ravelry.com/people/{}.json'.format(name), auth=requests.auth.HTTPBasicAuth(RAVELRY_USERNAME, RAVELRY_PASSWORD))
    return res.content

@app.route('/patterns')
def patterns():
    query = request.args
    pc = query.get('pc', '')
    weight = query.get('weight', '')
    view = query.get('view', '')
    sort = query.get('sort', '')
    fit = query.get('fit', '')
    craft = query.get('craft', '')
    colors = query.get('colors', '')

    res = requests.get('https://api.ravelry.com/patterns/search.json?pc={}&weight={}&view={}&sort={}&fit={}&craft={}&colors={}'.format(pc, weight, view, sort, fit, craft, colors), auth=requests.auth.HTTPBasicAuth(RAVELRY_USERNAME, RAVELRY_PASSWORD))
    return res.content

if __name__ == '__main__':
    app.run(debug=True)

