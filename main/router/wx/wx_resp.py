#!/usr/bin/env python
# -*- coding: utf-8 -*-

from main import app
from main.router.wx.wx_utils import init_wechat_sdk


def wechat_response(data):
    """微信消息处理回复"""
    global message, openid, wechat
    app.logger.info('----wechat msg :---\n' + data)
    wechat = init_wechat_sdk()
    wechat.parse_data(data)
    message = wechat.get_message()
    openid = message.source
    try:
        get_resp_func = msg_type_resp[message.type]
        response = get_resp_func()
    except KeyError:
        response = 'success'

    return response


# 储存微信消息类型所对应函数（方法）的字典
msg_type_resp = {}


def set_msg_type(msg_type):
    """
    储存微信消息类型所对应函数（方法）的装饰器
    """

    def decorator(func):
        msg_type_resp[msg_type] = func
        return func

    return decorator


@set_msg_type('subscribe')
def event_resp():
    """关注/取消关注事件回复"""
    app.logger.info('--------用户关注------')
    # response = wechat.response_image('6xbcktgL5KVQDsNjXNrAxYW3-PLYucb1on6Rpdf5I_Y')
    response = wechat.response_text("""欢迎关注能数跑腿侠 [玫瑰][玫瑰][玫瑰]

轻松做任务，现金、加油券任你领!!!

点击开始赚钱：http://u2p5hudl5iyp65ef.mikecrm.com/TaB6cIw

跑腿侠，GO GO GO!""")
    app.logger.info(response)
    return response


@set_msg_type('text')
def text_resp():
    """文本类型回复"""
    # 默认回复微信消息
    response = 'success'
    return response


@set_msg_type('click')
def click_resp():
    """菜单点击类型回复"""
    response = 'success'
    return response


@set_msg_type('scancode_waitmsg')
def scancode_waitmsg_resp():
    """扫码类型回复"""
    response = 'success'
    return response


def update_menu_setting():
    """更新自定义菜单"""
    try:
        menu_update_resp = init_wechat_sdk().create_menu(app.config['MENU_SETTING'])
        app.logger.info('update menu list: %s', menu_update_resp)
    except Exception, e:
        app.logger.error('Unhandled Exception: %s', e)
        return 'error'
    else:
        return 'success'
