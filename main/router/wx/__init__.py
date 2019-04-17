# coding=utf-8
from main import app, request, jsonify, url_param, uuid, time, mongo
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
    user = wl.user_info(access_token, openid)
    return jsonify(user)


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
