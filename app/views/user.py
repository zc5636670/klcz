#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask import Blueprint
from flask import g, request, flash, current_app
from flask import render_template, redirect, url_for
from ..utils.user import *
from ..forms.restaurant import *
from ..models.game import Game
from ..models.discount import Discount
import json
__all__ = ['bp']

bp = Blueprint('user', __name__)


@bp.route('/', methods=['GET', 'POST'])
@require_user
def home():
    user = Account.query.get(g.user.id)
    discount = Discount.query.filter_by(uid=g.user.id)
    dids = map(lambda o:o.gid,discount)
    games = Game.query.filter(Game.id.in_(dids))
    return render_template('user/home.html', user=user,games=games)


@bp.route('/setting', methods=['GET', 'POST'])
@require_user
def setting():
    """Settings page of current user."""
    user = g.user
    form = UserSettingForm(obj=user)
    next_url = request.args.get('next', url_for('.setting'))
    if form.validate_on_submit():
        user = Account.query.get(g.user.id)
        form.populate_obj(user)
        user.save()
        flash('Your profile is updated.')
        return redirect(next_url)
    return render_template('user/setting.html', form=form, user=user)


@bp.route('/add_game',methods=['get','post'])
@require_user
def add_game():
    user = g.user
    allgames = Game.query.filter_by(online='1').all()
    discounts = Discount.query.filter_by(uid=g.user.id).all()
    installed_game = map(lambda o: o.uid, discounts)
    return render_template('user/add_game.html', allgames=allgames, installed_game=installed_game)


@bp.route('/user_add_game_<gid>',methods=['get','post'])
@require_user
def add_game_handle(gid):
    discount = Discount()
    discount.uid = g.user.id
    discount.gid = gid
    Discount.save(discount)
    discount = Discount.query.filter_by(uid=g.user.id,gid=gid).all()[0]
    return redirect('user/discount_setting_'+discount.id)


@bp.route('/discount_setting_<did>',methods=['get','post'])
@require_user
def setting_discount(did):
    discount = Discount.query.filter_by(id=did).all()[0]
    _game = Game.query.filter_by(id=discount.gid).one()
    info = json.loads(_game.info_need)
    return render_template('user/setting_discount.html', info=info,did=did)

@bp.route('/get_discount_info_<did>_<info>',methods=['get','post'])
@require_user
def get_discount_info(did, info):
    discount = Discount.query.filter_by(id=did).one()
    discount.info = info
    Discount.save(discount)
    return 'ok'


