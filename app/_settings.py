#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os

DEBUG = False
TESTING = False
VERIFY_EMAIL = True
VERIFY_USER = True

ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))
# if os.path.exists('public/static'):
#     STATIC_FOLDER = os.path.join(os.getcwd(), 'public', 'static')
# else:
#     STATIC_FOLDER = os.path.join(ROOT_FOLDER, 'public', 'static')
#
# #: site

SECRET_KEY = 'secret key'
PASSWORD_SECRET = 'password secret'
GRAVATAR_BASE_URL = 'http://www.gravatar.com/avatar/'
GRAVATAR_EXTRA = ''

#: sqlalchemy
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:Zcwd1986@localhost/ooxx?charset=utf8'

STATIC_FOLDER = 'public/statics/'
SITE_TITLE = '快乐餐桌'
SITE_URL = '/'
