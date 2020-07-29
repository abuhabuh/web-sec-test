import json

import flask
from flask_cors import CORS, cross_origin


app = flask.Flask(__name__)

"""
The CORS spec here dictates what requests are processed from 
another origin.

* POST /name via default Content-Type (or any Content-Type that 
  does not trigger a preflight request) is always processed 
  regardless of CORS being active or the method specified in 
  the CORS `resources` section. The response (without CORS 
  auth) will be dropped by the web client, but the POST command 
  will have been executed by this server.

* GET /name 
  * Will be processed by this server regardless of CORS because 
    it is a "simple request".
  * If the web client will drop the response if CORS headers are 
    not specified by this server via the flask_cors.CORS config

"""
CORS(app,
    resources={
        '/name': {
            'origins': ['http://localhost:5001'], 
            'methods': ['GET', 'POST'],
        }
    },
)


NAME = 'john wang'


@app.route('/')
def get_root():
    return 'hello from resource server'


@app.route('/name', methods=['GET'])
def get_name():
    global NAME

    resp = {
        'name': NAME,
    }
    return json.dumps(resp)


@app.route('/name', methods=['POST'])
def post_name():
    global NAME

    new_name = flask.request.args.get('new_name', '')
    status = 'fail'
    if new_name:
        NAME = new_name
        status = 'success'

    resp = {
        'status': status,
        'name': NAME,
    }
    return json.dumps(resp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

