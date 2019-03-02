from flask import Flask

from endpoint.user import user_api

app = Flask(__name__)


def setup_blueprint():
    app.register_blueprint(user_api)

def setup():
    setup_blueprint()

setup()
