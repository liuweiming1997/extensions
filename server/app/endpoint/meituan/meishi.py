import flask
from flask import jsonify

from models.meituan.meishi import Meishi
from .base import MEITUAN_MEISHI_BASE_URL
from endpoint.decorator_tool import parse_user

meishi_api = flask.Blueprint('/meituan/meishi', __name__, url_prefix='/meituan/meishi')

@meishi_api.route('/', methods=['GET'])
@parse_user()
def get_all_meishi():
    meishi_list = Meishi.get_all_meishi()
    return jsonify([meishi.to_json() for meishi in meishi_list])

@meishi_api.route('/<meishi_poiid>/', methods=['GET'])
@parse_user()
def get_meishi_by_poiid(meishi_poiid):
    return jsonify({
        'meishiUrl': '{base_url}{meishi_poiid}/'.format(
            base_url=MEITUAN_MEISHI_BASE_URL,
            meishi_poiid=meishi_poiid,
        )
    })
