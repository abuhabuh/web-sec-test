import json


def add_endpoints(flask_app, jinja_env):

    @flask_app.route('/attack', methods=['GET'])
    def get_attack():
        return jinja_env.get_template('attack.html').render()

