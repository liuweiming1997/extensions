from flask import Flask
from flask_cors import CORS

from common.lib.errors.expection_base import ChromeServerExpectionBase
from common.lib.errors.error_handler import chrome_server_error_handler
from endpoint.user import user_api

app = Flask(__name__)

def setup_error_handler():
    app.register_error_handler(ChromeServerExpectionBase, chrome_server_error_handler)

def setup_blueprint():
    app.register_blueprint(user_api)

def setup():
    CORS(app, supports_credentials=True)
    setup_error_handler()
    setup_blueprint()

setup()
