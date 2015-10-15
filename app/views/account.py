from flask import Blueprint
from flask import request, flash, current_app
from flask import render_template, redirect, url_for, g
from ..forms.account import SignupForm, SigninForm
from ..utils.user import *
__all__ = ['bp']

bp = Blueprint('account', __name__)


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    next_url = request.args.get('next', url_for('.setting'))
    token = request.args.get('token')
    if token:
        user = verify_auth_token(token, 1)
        if not user:
            flash('Invalid or expired token.', 'error')
            return redirect(next_url)
        user.role = 'user'
        user.save()
        login_user(user)
        flash('This account is verified.', 'success')
        return redirect(next_url)

    form = SignupForm()
    if form.validate_on_submit():
        user = form.save()
        login_user(user)
        return redirect(next_url)
    return render_template('account/signup.html', form=SignupForm())

@bp.route('/setting', methods=['GET', 'POST'])
def setting():
    u = get_current_user()
    return redirect('/'+u.role+'/')


@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    """Sign in page."""
    next_url = request.args.get('next', '/')
    if g.user:
        return redirect(next_url)
    form = SigninForm()
    if form.validate_on_submit():
        login_user(form.user, form.permanent.data)
        return redirect(next_url)
    return render_template('account/signin.html', form=form)



@bp.route('/signout')
def signout():
    """Sign out, and redirect."""
    next_url = request.args.get('next', '/')
    logout_user()
    return redirect(next_url)

