#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import current_app
from flask_wtf import Form
from wtforms import TextField, PasswordField, BooleanField,StringField, SelectField,TextAreaField
from wtforms.validators import DataRequired,  Length
__all__ = [
    'ChooseForRole', 'AddGame'
]
class ChooseForRole(Form):
    phone = StringField('phone', validators=[DataRequired(), Length(min=11, max=11)])
    role = SelectField('role',
                       description='用户角色', choices=[
                            ('new', '未验证'),
                            ('user', '商户'),
                            ('staff', '员工'),
                            ('admin', '管理员')
                        ], default='user', validators=[DataRequired()])

class AddGame(Form):
    name = StringField('name')
    description = TextAreaField('description')
    template = StringField('template')
    info_need = TextAreaField('info_need')
    online = StringField('online')

