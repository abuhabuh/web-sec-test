import json

import flask
from jinja2 import Environment, FileSystemLoader, select_autoescape


def add_apis(flask_app, jinja_env):

    @flask_app.route('/')
    def get_root():
        # return jinja_env.get_template('index.html').render()
        cookie_attrs = {
            'Name': 'mycookie',
            'Secure': False,
            'HttpOnly': True,
            'SameSite': 'strict',
        }
        resp = flask.make_response(
            json.dumps({
                'foo': 'bar',
                'cookie_attrs': cookie_attrs,
            })
        )

        return resp
