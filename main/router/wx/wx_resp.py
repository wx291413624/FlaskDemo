#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from main import app
from main.router.wx.wx_utils import init_wechat_sdk


def wechat_response(data):
    """微信消息处理回复"""
    global message, openid, wechat

    wechat = init_wechat_sdk()
    wechat.parse_data(data)
    message = wechat.get_message()
    openid = message.source
    # 用户信息写入数据库

    try:
        get_resp_func = msg_type_resp[message.type]
        response = get_resp_func()
    except KeyError:
        # 默认回复微信消息
        response = 'success'

    # 保存最后一次交互的时间
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


@set_msg_type('subscribe')
def subscribe_resp():
    """订阅类型回复"""
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
