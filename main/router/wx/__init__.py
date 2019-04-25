# coding=utf-8
import json

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
    openid = data.openid
    access_token = data.access_token
    wechat_user = wl.user_info(access_token, openid)
    account = User.query.filter_by(openid=wechat_user.openid).first()
    if account:
        app.logger.info('----user is in our database---')
    else:
        account = User(unionid=wechat_user.unionid, openid=wechat_user.openid, nickName=wechat_user.nickname,
                       head_img_url=wechat_user.headimgurl, sex=wechat_user.sex, is_del=0, isErrandsMan=0).save()
    token = str.replace(str(uuid.uuid1()), '-', '')
    redis.set("account:wechat_login:" + token, json.dumps(account.to_json()), 70000)
    if wechat_user.phone:
        return jsonify({'token': token, 'type': 1})
    return jsonify({'token': token, 'type': 0})


@app.route("/menu", methods=['GET', 'POST'])
@url_param
def menu():
    """wechat menu"""
    wx_resp.update_menu_setting()
    return 'success'


@app.route("/wechat/upload", methods=['GET', 'POST'])
@url_param
def upload():
    """微信上传图片"""
    fs = request.files.getlist('file')
    pic_list = []
    for f in fs:
        uid = uuid.uuid1()
        name = str.replace(str(uid), '-', '')
        access_token = get_wechat_access_token()
        data = wechat_login("", "").upload_file(access_token, f, name, 'image')
        ss = {'data': time.time(), 'uuid': str.replace(str(uid), '-', ''), 'pic': data}
        mongo.db.wechatpic.insert_one(ss)
        pic_list.append(data)
    return pic_list
