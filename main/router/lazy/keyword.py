# coding=utf-8
import datetime
import json

from flask import render_template

from main import app, jsonify, request, redis
from main.models.wechat_model import WechatMaterial
from main.router.lazy import check_login
from main.router.wx import get_wechat_access_token, wechat_login


@app.route("/keyword", methods=['GET'])
@check_login
def ex_keyword():
    list, mate_list = get_list()
    return render_template('keyword/keyword.html', list=list, mate_list=mate_list)


def get_list():
    key_list = redis.keys('keyword:back:*')
    va_list = []
    for key in key_list:
        list = redis.hgetall(key)
        va_list.append({'key': str(key).replace('keyword:back:', ''), 'value': list})
    mate_list = WechatMaterial.query.filter_by(state=0).order_by(WechatMaterial.create_time.desc())
    return va_list, mate_list


@app.route("/keyword/del", methods=['POST'])
@check_login
def ex_keyword_del():
    value = request.form.get('value')
    redis.hdel('keyword:all', value)
    list, mate_list = get_list()
    return render_template('keyword/keyword.html', list=list, mate_list=mate_list)


@app.route("/keyword/insert", methods=['POST'])
@check_login
def ex_keyword_def_insert():
    media_ids = request.form.get('mediaIds')
    key = request.form.get('mediaKey')
    media_ids = json.loads(media_ids)
    for media_id in media_ids:
        redis.hset('keyword:back:' + key, media_id['id'].replace('\n', '').strip(), media_id['type'])
    list, mate_list = get_list()
    return render_template('keyword/keyword.html', list=list, mate_list=mate_list)
