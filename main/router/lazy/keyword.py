# coding=utf-8
import datetime

from flask import render_template

from main import app, jsonify, request, redis
from main.models.wechat_model import WechatMaterial
from main.router.lazy import check_login
from main.router.wx import get_wechat_access_token, wechat_login


@app.route("/keyword", methods=['GET'])
@check_login
def ex_keyword():
    list = get_list()
    return render_template('keyword/keyword.html', list=list)


def get_list():
    list = redis.hgetall('keyword:all')
    key_list = []
    for li in list:
        ls = {"key": li, "value": list[li]}
        key_list.append(ls)
    return key_list


@app.route("/keyword/insert", methods=['POST'])
@check_login
def ex_keyword_insert():
    type = request.form.get('type')
    value = request.form.get('value')
    redis.hset('keyword:all', value, type)
    list = get_list()
    return render_template('keyword/keyword.html', list=list)


@app.route("/keyword/del", methods=['POST'])
@check_login
def ex_keyword_del():
    value = request.form.get('value')
    redis.hdel('keyword:all', value)
    list = get_list()
    return render_template('keyword/keyword.html', list=list)
