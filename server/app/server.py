from flask import Flask
from flask_cors import CORS

from config import config
from common.lib.errors.expection_base import ChromeServerExpectionBase
from common.lib.errors.error_handler import chrome_server_error_handler
from endpoint.meituan.meishi import meishi_api
from endpoint.user import user_api
from endpoint.douban.dianying import dianying_api

app = Flask(__name__)

def setup_error_handler():
    app.register_error_handler(ChromeServerExpectionBase, chrome_server_error_handler)

def setup_blueprint():
    app.register_blueprint(user_api)
    app.register_blueprint(dianying_api)
    app.register_blueprint(meishi_api)

def setup():
    CORS(app, supports_credentials=True)
    app.config['SECRET_KEY'] = config.SECRET_KEY
    app.config['JSON_AS_ASCII'] = config.JSON_AS_ASCII
    app.config['JSON_SORT_KEYS'] = config.JSON_SORT_KEYS
    app.config["SESSION_COOKIE_HTTPONLY"] = config.SESSION_COOKIE_HTTPONLY
    setup_error_handler()
    setup_blueprint()

setup()
