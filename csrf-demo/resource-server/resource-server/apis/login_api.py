import json
import logging

import flask

from apis.accounts_api import THE_BANK


LOG = logging.getLogger(__name__)


def add_endpoints(flask_app, jinja_env):

    @flask_app.route('/login', methods=['GET'])
    def get_login():
        return jinja_env.get_template('login.html').render()

    @flask_app.route('/login', methods=['POST'])
    def post_login():
        name = flask.request.form.get('name')
        if name in THE_BANK:
            resp = flask.make_response(flask.redirect('/accounts', code=302))
            resp.set_cookie('username', name)
            LOG.info(f'{name} logged in')
        else:
            resp = flask.make_response('no match found')
            LOG.info(f'{name} not found')
        return resp

