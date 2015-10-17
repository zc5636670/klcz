#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import time
import datetime
import logging
import hashlib
from flask import Flask, g
from models import *

def create_app():
    app = Flask(__name__)
    app = register_routes(app)
    app.config.from_pyfile('_settings.py')
    return app


def register_routes(app):
    from views import front, user, staff, admin, account,game
    app.register_blueprint(account.bp, url_prefix='/account')
    app.register_blueprint(staff.bp, url_prefix='/staff')
    app.register_blueprint(user.bp, url_prefix='/user')
    app.register_blueprint(admin.bp, url_prefix='/admin')
    app.register_blueprint(game.bp, url_prefix='/game')
    app.register_blueprint(front.bp, url_prefix='')
    return app
def register_database(app):
    """Database related configuration."""
    #: prepare for database
    db.init_app(app)
    db.app = app
    db.create_all()
    #: prepare for cache


def register_hooks(app):
    """Hooks for request."""
    from .utils.user import get_current_user

    @app.before_request
    def load_current_user():
        g.user = get_current_user()
        if g.user and g.user.is_staff:
            g._before_request_time = time.time()

    @app.after_request
    def rendering_time(response):
        if hasattr(g, '_before_request_time'):
            delta = time.time() - g._before_request_time
            response.headers['X-Render-Time'] = delta * 1000
        return response

def start():
    app = create_app()
    register_database(app)
    register_hooks(app)
    app.debug = True
    app.run()

