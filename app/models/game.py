# coding: utf-8

import hashlib
from datetime import datetime
from werkzeug import security
from ._base import db, SessionMixin

__all__ = ('Account', 'NonAccount')


class Game(db.Model, SessionMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, index=True, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    template = db.Column(db.String(80))
    info_need = db.Column(db.TEXT)
    online = db.Column(db.String(1), default='0')

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
            setattr(self, k, v)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Account: %s>' % self.name


