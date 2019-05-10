# coding=utf-8
import datetime

from flask import render_template

from main import app, jsonify, request, redis
from main.models.wechat_model import WechatMaterial
from main.router.lazy import check_login
from main.router.wx import get_wechat_access_token, wechat_login


@app.route("/follow", methods=['GET'])
@check_login
def ex_follow():
    msg = get_msg()
    return render_template('follow/follow.html', msg=msg)


def get_msg():
    msg = redis.get('follow:msg').replace('\n', '</br>')
    return msg


@app.route("/follow/up", methods=['POST'])
@check_login
def ex_follow_up():
    value = request.form.get('value')
    redis.set('follow:msg', value)
    msg = get_msg()
    return render_template('follow/follow.html', msg=msg)
