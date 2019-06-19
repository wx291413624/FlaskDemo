# coding=utf-8
import json
import time
import datetime

from flask import jsonify, request, render_template
from flask_pymongo import DESCENDING

from main import app, mongo, wx_mongo
from main.router.lazy import check_login


@app.route("/log", methods=['GET'])
@check_login
def log_wx():
    filters = {}
    gas = wx_mongo.db.requestlog.find(filters)
    print gas
    for gg in gas:
        print gg
    return "123"
