import logging

import flask

from apis import accounts_api
from apis import base_api
from apis import login_api


def bootstrap_app(jinja_env):
    flask_app = flask.Flask(__name__)
    
    base_api.add_endpoints(flask_app, jinja_env)
    accounts_api.add_endpoints(flask_app, jinja_env)
    login_api.add_endpoints(flask_app, jinja_env)

    logging.basicConfig(level=logging.INFO)

    return flask_app

