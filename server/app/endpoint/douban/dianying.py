import flask
from flask import jsonify

from models.douban.dianying import Dianying
from endpoint.decorator_tool import parse_user

dianying_api = flask.Blueprint('/douban/dianying', __name__, url_prefix='/douban/dianying')

@dianying_api.route('/onshow/', methods=['GET'])
@parse_user()
def get_onshow_movie():
    onshow_movie_list = Dianying.get_onshow()
    return jsonify([onshow_movie.to_json() for onshow_movie in onshow_movie_list])

@dianying_api.route('/upcoming/', methods=['GET'])
@parse_user()
def get_upcoming_movie():
    upcoming_movie_list = Dianying.get_upcoming()
    return jsonify([upcoming_movie.to_json() for upcoming_movie in upcoming_movie_list])
