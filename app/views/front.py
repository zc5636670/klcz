from flask import Blueprint
from flask import g, request, flash, current_app
from flask import render_template, redirect, url_for
from ..models import *
__all__ = ['bp']

bp = Blueprint('front', __name__)


@bp.route('/', methods=['GET', 'POST'])
def home():
    return render_template('front/index.html', say='hello')

