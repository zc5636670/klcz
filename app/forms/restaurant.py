# coding: utf-8
from flask import current_app
from flask_wtf import Form
from wtforms import TextField, PasswordField, BooleanField,StringField
from wtforms import TextAreaField
from wtforms.fields.html5 import EmailField, URLField
from wtforms.validators import DataRequired, Email, Length, Regexp
from wtforms.validators import Optional, URL

from ..models import Account


class SettingForm(Form):
    screen_name = StringField('展示名称', validators=[Length(max=80)])
    full_name = StringField('全名', validators=[Length(max=80)])
    description = TextAreaField(
        '地址及其他介绍', validators=[Optional(), Length(max=400)],
        description='Markdown is supported.'
    )