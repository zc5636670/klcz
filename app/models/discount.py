# coding: utf-8
import datetime
from ._base import *

#__all__ = ('Discount')


class Discount(db.Model, SessionMixin):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, index=True)
    gid = db.Column(db.Integer, index=True)
    info = db.Column(db.TEXT)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
            setattr(self, k, v)

    def __str__(self):
        return str(self.uid)

    def __repr__(self):
        return '<Account: %s>' % str(self.uid)


class Play(db.Model,SessionMixin):
    id = db.Column(db.Integer, primary_key=True)
    start_when = db.Column(db.DateTime, default=datetime.datetime.now())
    player = db.Column(db.String(10))
    uid = db.Column(db.Integer, index=True)
    gid = db.Column(db.Integer, index=True)
    best_score = db.Column(db.Integer, index=True)

