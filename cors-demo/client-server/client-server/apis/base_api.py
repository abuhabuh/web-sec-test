import json

import flask
from jinja2 import Environment, FileSystemLoader, select_autoescape


def add_endpoints(flask_app, jinja_env):

    @flask_app.route('/')
    def get_root():
        return jinja_env.get_template('index.html').render()
