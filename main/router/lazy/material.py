# coding=utf-8
import datetime

from flask import render_template

from main import app, jsonify, request, redis
from main.models.wechat_model import WechatMaterial
from main.router.lazy import check_login
from main.router.wx import get_wechat_access_token, wechat_login


def find_list(page):
    if page is None:
        page = 1
    return WechatMaterial.query.order_by(WechatMaterial.create_time.desc()).paginate(page, 10)


@app.route("/material", methods=['GET'])
@check_login
def ex_material():
    page = request.form.get('page')
    var = find_list(page)
    return render_template('material/material.html', list=var.items)


@app.route("/material/upload", methods=['POST'])
@check_login
def ex_material_upload():
    materialType = request.form.get('materialType')
    type = request.form.get('type')
    desc = request.form.get('desc')
    key = request.form.get('key')
    fs = request.files.getlist('file')
    if fs is not None:
        access_token = get_wechat_access_token()
        data = wechat_login("", "").upload_file(access_token, fs[0], materialType)
        WechatMaterial(media_id=data['media_id'], url=data['url'], material_type=materialType, type=type,
                       create_time=datetime.datetime.now(), desc=desc, key=key, state=0, is_use=0).save()
        error = 'SUCCESS'
    else:
        error = 'ERROR'
    var = find_list(None)
    return render_template('material/material.html', error=error, list=var.items)


@app.route("/material/del", methods=['POST'])
@check_login
def ex_material_del():
    media_id = request.form.get('media_id')
    v = WechatMaterial.query.filter_by(media_id=media_id).first()
    if v.is_use == 1:
        error = 'this media is use'
    else:
        access_token = get_wechat_access_token()
        wechat_login("", "").del_file(access_token, media_id)
        v.is_use = 0
        v.state = 1
        v.update_commit()
        redis.delete('text:back:' + v.key)
        error = 'SUCCESS'
    var = find_list(None)
    return render_template('material/material.html', list=var.items, error=error)


@app.route("/material/use", methods=['POST'])
@check_login
def ex_material_use():
    media_id = request.form.get('media_id')
    v = WechatMaterial.query.filter_by(media_id=media_id).first()
    if v.state != 1:
        redis.set('text:back:' + v.key, media_id)
        v.is_use = 1
        v.update_commit()
    var = find_list(None)
    return render_template('material/material.html', list=var.items)


@app.route("/material/off", methods=['POST'])
@check_login
def ex_material_off():
    media_id = request.form.get('media_id')
    v = WechatMaterial.query.filter_by(media_id=media_id).first()
    if v is not None:
        redis_media_id = redis.get('text:back:' + v.key)
        if redis_media_id == media_id:
            redis.delete('text:back:' + v.key)
        v.is_use = 0
        v.update_commit()
    var = find_list(None)
    return render_template('material/material.html', list=var.items)
