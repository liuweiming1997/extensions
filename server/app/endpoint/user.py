import flask
from flask import jsonify, session, g

from models.user import User
from .decorator_tool import parse_user, parse_args

user_api = flask.Blueprint('user', __name__, url_prefix='/user')

@user_api.route('/load_or_create/', methods=['POST'])
@parse_args('username', str)
@parse_args('password', str)
def load_or_create(username, password):
    user_obj = User.load_or_create(username, password)
    session['user_id'] = user_obj.id
    return jsonify(user_obj.to_json())
