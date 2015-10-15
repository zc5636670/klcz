from flask import Blueprint
from flask import g, request, flash, current_app
from flask import render_template, redirect, url_for
from flask.ext.babel import gettext as _
__all__ = ['bp']

bp = Blueprint('user', __name__)


@bp.route('/', methods=['GET', 'POST'])
def home():
    return 'hello'

