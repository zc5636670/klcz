# coding: utf-8
# flake8: noqa

from ._base import *
from .account import *
from .discount import *
from .game import *
from flask.ext.sqlalchemy import models_committed


def get_by_ids(model, uids):
    if not len(uids):
        return {}

    if len(uids) == 1:
        data = model.query.get(uids.pop())
        return {data.id: data}

    data = model.query.filter(model.id.in_(uids)).all()
    ret = {}
    for item in data:
        ret[item.id] = item
    return ret


def create():
    db.create_all()