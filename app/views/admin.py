from flask import Blueprint
from flask import g, request, flash, current_app
from flask import render_template, redirect, url_for
from ..forms.admin import *
from ..utils.user import *
from ..models.account import Account
from ..models.game import Game
__all__ = ['bp']

bp = Blueprint('admin', __name__)


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/home', methods=['GET', 'POST'])
@require_admin
def home():
    return render_template('admin/home.html')



@bp.route('/m_role', methods=['POST', 'GET'])
@require_admin
def m_role():
    form = ChooseForRole()
    if form.validate_on_submit():
        user = Account.query.filter_by(phone=form.data.get('phone')).all()[0]
        user.role = form.data.get('role')
        user.save()
        return render_template('admin/m_staff.html', form=form, user=user.role)
    else:
        return render_template('admin/m_staff.html', form=form, user=get_current_user())



@bp.route('/m_game', methods=['POST', 'GET'])
@require_admin
def showgame():
    games = Game.query.all()
    return render_template('admin/m_game.html', games=games)


@bp.route('/m_add_game', methods=['POST', 'GET'])
@require_admin
def add_game():
    form = AddGame()
    if form.validate_on_submit():
        game = Game(**form.data)
        game.save()
        return render_template('admin/m_add_game.html',form=form, msg=form.data)
    return render_template('admin/m_add_game.html', form=form)


@bp.route('/update_game_<gameID>', methods=['POST', 'GET'])
@require_admin
def update_game(gameID):
    _game = Game.query.filter_by(id=gameID).one()
    form = AddGame()
    if form.validate_on_submit():
        form.populate_obj(_game)
        _game.save()
    return render_template('admin/m_update_game.html',game=_game,form=form)