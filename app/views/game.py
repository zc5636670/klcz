#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask import Blueprint
from flask import g, request, flash, current_app
from flask import render_template, redirect, url_for
from ..utils.user import *
from ..forms.restaurant import *
__all__ = ['bp']

bp = Blueprint('game', __name__)

