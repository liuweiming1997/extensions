import flask
from flask import jsonify
user_api = flask.Blueprint('user', __name__, url_prefix='/user')

@user_api.route('/', methods=['POST', 'GET'])
def user():
    return jsonify({
        "result": "ok"
    })
