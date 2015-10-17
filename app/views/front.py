from flask import Blueprint
from flask import g, request, flash, current_app
from flask import render_template, redirect, url_for
from ..models import *
__all__ = ['bp']

bp = Blueprint('front', __name__)


@bp.route('/', methods=['GET', 'POST'])
def home():
    return render_template('front/index.html', say='hello')


@bp.route('/play_<userID>_<gameID>', methods=['GET', 'POST'])
def play(userID='1',gameID='2'):
    _game = Game.query.filter_by(id=gameID).one()
    return render_template('game/play/dz2048.html',restaurant = {'name':'a'},game = {'name':'b'})

