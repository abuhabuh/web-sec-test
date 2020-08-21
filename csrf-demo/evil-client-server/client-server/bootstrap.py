import flask

from apis import base_api


def bootstrap_app(jinja_env):
    flask_app = flask.Flask(__name__)
    
    base_api.add_endpoints(flask_app, jinja_env)

    return flask_app

