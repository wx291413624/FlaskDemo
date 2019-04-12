# coding=utf-8
from flask import jsonify

from main import app


@app.errorhandler(404)
def page_not_found(error):
    return "page not found!", 404


@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.error('Unhandled Exception: %s', (error))
    return "Error", 500


@app.route("/router", methods=['GET'])
def router_get():
    router = [
        {
            'router': [
                {'url': '/token', 'param': [], 'remark': '获取access_token'},
                {'url': '/userid', 'param': ['token', 'code'], 'remark': '查询用户user_id'},
                {'url': '/user', 'param': ['token', 'userid'], 'remark': '获取用户信息'}
            ],
            'remark': '钉钉api'
        },
        {
            'router': [
                {'url': '/pic', 'param': ['file'], 'remark': '图片上传'}
            ],
            'remark': '图片api'
        },
        {
            'router': [
                {'url': '/insert', 'param': ['key'], 'remark': '录入信息'},
                {'url': '/find', 'param': ['page', 'name', 'tday'], 'remark': '查询信息'},
                {'url': '/put', 'param': ['uuid'], 'remark': '修改信息'}
            ],
            'remark': '加油站录入api'
        }
    ]
    return jsonify(router)
