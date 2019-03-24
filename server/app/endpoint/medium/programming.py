import flask
from flask import jsonify

from models.medium.programming import Programming
from endpoint.decorator_tool import parse_user

medium_programming_api = flask.Blueprint('/medium/programming', __name__, url_prefix='/medium/programming')

@medium_programming_api.route('/', methods=['GET'])
@parse_user()
def get_all_programming():
    programming_blogs = Programming.get_all_programming()
    return jsonify([blog.to_json() for blog in programming_blogs])
