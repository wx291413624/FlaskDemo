#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import db


class CUser(db.Model):
    __tablename__ = 'CUser'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cname = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(100), unique=True, nullable=False)
    baidux = db.Column(db.String(20), unique=True, nullable=False)
    baiduy = db.Column(db.String(20), unique=True, nullable=False)
    activity = db.Column(db.String(500), unique=True, nullable=False)
    payname = db.Column(db.String(100), unique=True, nullable=False)
    zzyqzl = db.Column(db.String(100), unique=True, nullable=False)
    fwlsmc = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self,  cname=None, address=None,
                 baidux=None,  baiduy=None, activity=None,
                 payname=None, zzyqzl=None, fwlsmc=None):
        self.cname = cname
        self.address = address
        self.baidux = baidux
        self.baiduy = baiduy
        self.activity = activity
        self.payname = payname
        self.zzyqzl = zzyqzl
        self.fwlsmc = fwlsmc

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict