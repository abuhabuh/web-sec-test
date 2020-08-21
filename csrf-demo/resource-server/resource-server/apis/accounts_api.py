import json

import flask


THE_BANK = {
    'alice': 5000,
    'chuck': 1000,
}


def add_endpoints(flask_app, jinja_env):

    @flask_app.route('/accounts', methods=['GET'])
    def get_accounts():
        global THE_BANK
        return json.dumps(THE_BANK, indent=2)

    @flask_app.route('/transfer', methods=['POST'])
    def post_transfer():
        from_id = flask.request.args.get('from')
        to_id = flask.request.args.get('to')
        amt = int(flask.request.args.get('amt'))

        global THE_BANK
        if from_id in THE_BANK and to_id in THE_BANK and \
                THE_BANK[from_id] >= amt:
            THE_BANK[from_id] = THE_BANK[from_id] - amt
            THE_BANK[to_id] = THE_BANK[to_id] + amt

        return json.dumps(THE_BANK, indent=2)
