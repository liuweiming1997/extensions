from flask import Flask

from common.lib.errors.expection_base import ChromeServerExpectionBase
from common.lib.errors.error_handler import chrome_server_error_handler
from endpoint.user import user_api

app = Flask(__name__)

def setup_error_handler():
    app.register_error_handler(ChromeServerExpectionBase, chrome_server_error_handler)

def setup_blueprint():
    app.register_blueprint(user_api)

def setup():
    setup_error_handler()
    setup_blueprint()

setup()
