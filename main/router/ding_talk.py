import requests

from main import app, jsonify, request


@app.route("/token", methods=['GET', 'POST'])
def token():
    info_res = requests.get(
        "https://oapi.dingtalk.com/gettoken?appkey=dingtcftqzrv7cicm6rw&appsecret=w1"
        "-ixtw_3u38YsYwvPYQu2SkCX0gY9MY4NHe97UqtMgCOwlJhhZDzFsWtcMEq_Gp")
    return jsonify(info_res.json())


@app.route("/userid", methods=['GET', 'POST'])
def user_id():
    access_token = request.args.get('token')
    code = request.args.get('code')
    info_res = requests.get("https://oapi.dingtalk.com/user/getuserinfo?access_token=" + access_token + "&code=" + code)
    return jsonify(info_res.json())


@app.route("/user", methods=['GET', 'POST'])
def user():
    access_token = request.args.get('token')
    userid = request.args.get('userid')
    info_res = requests.get("https://oapi.dingtalk.com/user/get?access_token=" + access_token + "&userid=" + userid)
    return jsonify(info_res.json())
