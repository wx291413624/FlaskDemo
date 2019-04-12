# coding=utf-8
from main import app, request, jsonify
from main.router.wx.wx_login import wechat_login
from main.router.wx.wx_resp import wechat_response
from main.router.wx.wx_utils import check_signature


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
    code = request.args.get("code")
    if not code:
        return "ERR_INVALID_CODE", 400
    wl = wechat_login(app.config['APP_ID'], app.config['APP_SECRET'])
    data = wl.access_token(code)
    openid = data.openid
    access_token = data.access_token
    user = wl.user_info(access_token, openid)
    return jsonify(user)
