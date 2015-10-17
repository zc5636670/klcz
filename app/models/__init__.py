# coding: utf-8
# flake8: noqa
#CREATE DATABASE ooxx DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
from ._base import *
from .account import *
from .discount import *
from .game import Game
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