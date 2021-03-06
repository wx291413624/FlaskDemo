# coding=utf-8
import json
import re

from main import app, request, jsonify, url_param, uuid, time, mongo, redis
from main.models.model import User, ErrandsManIdentity
from main.router.wx.wx_login import wechat_login
from main.router.wx.wx_resp import wechat_response
from main.router.wx.wx_utils import check_signature, get_wechat_access_token


@app.route("/weixin", methods=['GET', 'POST'])
@check_signature
def handle_wechat_request():
    """
    处理回复微信请求
    """
    if request.method == 'POST':
        return wechat_response(request.data)
    else:
        # 微信接入验证
        return request.args.get('echostr', '')


@app.route("/authorized", methods=['GET', 'POST'])
def authorized():
    """get openid"""
    code = request.args.get("code")
    if not code:
        return "ERR_INVALID_CODE", 400
    wl = wechat_login(app.config['APP_ID'], app.config['APP_SECRET'])
    data = wl.access_token(code)
    app.logger.info(data)
    openid = data['openid']
    access_token = data['access_token']
    wechat_user = wl.user_info(access_token, openid)
    app.logger.info(wechat_user)
    account = User.query.filter_by(openid=wechat_user['openid']).first()
    if account:
        app.logger.info('----user is in our database---')
    else:
        unionid = ''
        if 'unionid' in wechat_user:
            unionid = wechat_user['unionid']
        account = User(unionid=unionid, openid=wechat_user['openid'], nick_name=str(wechat_user['nickname']),
                       head_img_url=wechat_user['headimgurl'], sex=wechat_user['sex'], is_del=0,
                       is_errands_man=0).save()
    token = str.replace(str(uuid.uuid1()), '-', '')
    redis.set("account:wechat_login:" + token, json.dumps(account.to_json()), 72000)
    if account.phone:
        return jsonify({'token': token, 'type': 1})
    return jsonify({'token': token, 'type': 0})


@app.route("/menu", methods=['GET', 'POST'])
@url_param
def menu():
    """wechat menu"""
    wx_resp.update_menu_setting()
    return 'success'


def have_img(keyword):
    print type(keyword) == unicode
    img_re = re.compile(u'['u'\U0001F300-\U0001F64F'u'\U0001F680-\U0001F6FF'u'\u2600-\u2B55]+', re.UNICODE)
    return img_re.split(keyword)


def check_url(url):
    ul = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx2f772ca355796adb&redirect_uri=" + url + "&response_type=code&scope=snsapi_userinfo&state=STATE&connect_redirect=1#wechat_redirect"
