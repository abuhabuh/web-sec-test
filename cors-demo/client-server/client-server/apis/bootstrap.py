import flask

from apis import base


def bootstrap_app(jinja_env):
    flask_app = flask.Flask(__name__)
    
    base.add_apis(flask_app, jinja_env)

    return flask_app

