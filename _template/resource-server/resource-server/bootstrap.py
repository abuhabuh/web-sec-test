import flask
from flask_cors import CORS, cross_origin

from apis import base_api


def bootstrap_app(jinja_env):
    flask_app = flask.Flask(__name__)
    
    base_api.add_endpoints(flask_app, jinja_env)

    return flask_app


def add_cors(app):
    """
    DEPRECATED

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
      * The web client will drop the response if CORS headers are 
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
