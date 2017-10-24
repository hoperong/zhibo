#!/usr/bin/env python
# coding=utf-8

from flask import Flask


def create_app():
    app = Flask(__name__)

    # route
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    from .controller import controller as controller_blueprint
    app.register_blueprint(controller_blueprint)

    return app
