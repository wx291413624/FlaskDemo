# coding=utf-8
import json
import re
import time
import uuid
import datetime

from flask import jsonify, request
from flask_pymongo import DESCENDING

from main import app, mongo
from main.utils import DecimalEncoder
from main.utils.req import url_param
from main.models.czb_model import YfqFwGasInfo


@app.route("/insert", methods=['POST'])
@url_param
def insert_gas():
    key = request.form.get('key')
    if key is None:
        return 'error'
    app.logger.info("-----数据录入--")
    uid = uuid.uuid1()
    app.logger.info("-----" + key)
    json_to_python = json.loads(key)
    user = json_to_python['user']
    unionid = user["unionid"]
    ss = {'unionid': unionid, 'gas': key, 'data': time.time(), 'type': 1, 'uuid': str.replace(str(uid), '-', '')}
    mongo.db.dingtalkgas.insert_one(ss)
    app.logger.info("--------录入成功---------")
    return 'success'


@app.route("/find", methods=['GET', 'POST'])
@url_param
def find_gas_list():
    filters = {}
    page = request.args.get('page')
    name = request.args.get('name')
    tday = request.args.get('tday')
    if tday is not None:
        start_time = int(time.mktime(time.strptime(str(tday), '%Y-%m-%d')))
        ddd = datetime.datetime.strptime(tday, '%Y-%m-%d')
        tomorrow = ddd + datetime.timedelta(days=1)
        end_time = int(time.mktime(time.strptime(str(tomorrow.strftime('%Y-%m-%d')), '%Y-%m-%d')))
        filters['data'] = {'$gte': start_time, '$lte': end_time}
    if name is not None:
        rex_exp = re.compile('.*' + str(name) + '.*', re.IGNORECASE)
        filters['gas'] = rex_exp
    if page is None:
        gas = mongo.db.dingtalkgas.find(filters).sort('data', DESCENDING)
    else:
        page = int(page)
        if page < 1:
            page = 0
        else:
            page = 10 * (page - 1)
        gas = mongo.db.dingtalkgas.find(filters).sort('data', DESCENDING).limit(10).skip(page)
    count = mongo.db.dingtalkgas.find(filters).count()
    gas_list = []
    for g in gas:
        g.pop('_id')
        g['data'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(g['data'])))
        gas_list.append(g)
    all_list = {'count': count, 'gasList': gas_list}
    return jsonify(all_list)


@app.route("/put", methods=['GET', 'POST'])
def put_gas():
    gas_uuid = request.args.get('uuid')
    if gas_uuid is None:
        return 'error'
    mongo.db.dingtalkgas.update_one({'uuid': gas_uuid}, {'$set': {'type': 2}})
    gas = mongo.db.dingtalkgas.find_one({'uuid': gas_uuid})
    json_to_python = json.loads(gas['gas'])
    ss = json_to_python['user']
    print ss
    return 'success'


@app.route("/czb/gas", methods=['GET'])
def gas_get_sql():
    pwd = request.args.get('pwd')
    if pwd is not None and pwd == 'czbgas':
        lat = request.args.get('lat')
        lng = request.args.get('lng')
        gas = YfqFwGasInfo().find_sum(lat, lng)
        gas_list = []
        for ga in gas:
            gas_list.append(json.dumps(list(ga), cls=DecimalEncoder))
        return jsonify(gas_list)
    else:
        return jsonify([])
