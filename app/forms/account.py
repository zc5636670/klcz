#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import current_app
from flask_wtf import Form
from wtforms import TextField, PasswordField, BooleanField,StringField
from wtforms.validators import DataRequired, Email, Length, Regexp

from ..models import Account

__all__ = [
    'SignupForm', 'SigninForm',
    #'SettingForm',
    #'FindForm', 'ResetForm',
]

RESERVED_WORDS = [
    'root', 'admin', 'bot', 'robot', 'master', 'webmaster',
    'account', 'people', 'user', 'users', 'project', 'projects',
    'search', 'action', 'favorite', 'like', 'love', 'none',
    'team', 'teams', 'group', 'groups', 'organization',
    'organizations', 'package', 'packages', 'org', 'com', 'net',
    'help', 'doc', 'docs', 'document', 'documentation', 'blog',
    'bbs', 'forum', 'forums', 'static', 'assets', 'repository',

    'public', 'private',
    'mac', 'windows', 'ios', 'lab',
]


class SignupForm(Form):
    phone = StringField(
        'phone', validators=[
            DataRequired(), Length(min=11, max=11),
            Regexp(r'^[0-9]+$')
        ], description='请输入数字.',
    )
    password = PasswordField(
        'Password', validators=[DataRequired()]
    )

    def validate_phone(self, field):
        data = field.data.lower()
        if Account.query.filter_by(phone=data).count():
            raise ValueError('已被注册的手机号')

    def save(self, role=None):
        user = Account(**self.data)
        if role:
            user.role = role
        user.save()
        return user


class SigninForm(Form):
    account = StringField(
        'Account',
        validators=[DataRequired(), Length(min=11, max=11)],
        description='phoneNumber'
    )
    password = PasswordField(
        'Password', validators=[DataRequired()]
    )
    permanent = BooleanField('保存一个月')

    def validate_password(self, field):
        account = self.account.data
        user = Account.query.filter_by(phone=account).first()
        if not user:
            raise ValueError('未注册的手机号')
        if user.check_password(field.data):
            self.user = user
            return user
        raise ValueError('Wrong account or password')



