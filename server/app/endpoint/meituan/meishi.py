import flask
from flask import jsonify
meishi_api = flask.Blueprint('/meituan/meishi', __name__, url_prefix='/meituan/meishi')

@meishi_api.route('/', methods=['GET'])
def get_all_meishi():
    return jsonify({
        "result": "ok"
    })
