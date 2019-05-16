#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from main import app, re, redis
from main.router.wx.wx_utils import init_wechat_sdk

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


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
    response = wechat.response_text(redis.get('follow:msg'))
    app.logger.info(response)
    return response


@set_msg_type('text')
def text_resp():
    """文本类型回复"""
    message.content = message.content.replace(u'　', ' ')
    message.content = message.content.lstrip()
    list = redis.hgetall('keyword:back:' + message.content)
    openid = message.source
    response = ''
    if len(list) > 1:
        for li in list:
            msg_type = json.loads(list[li])['type']
            if msg_type == 'image':
                wechat.send_image_message(openid, li)
            if msg_type == 'video':
                wechat.send_video_message(openid, li)
            if msg_type == 'voice':
                wechat.send_voice_message(openid, li)
            if msg_type == 'text':
                wechat.send_text_message(openid, li)
    elif len(list) == 1:
        key_frist = list.keys()[0]
        msg_type = json.loads(list[key_frist])['type']
        if msg_type == 'image':
            response = return_to_pic(key_frist)
        elif msg_type == 'video':
            response = return_to_video(key_frist)
        elif msg_type == 'voice':
            response = return_to_voice(key_frist)
        elif msg_type == 'text':
            response = return_to_text(key_frist)
    return response


@set_msg_type('click')
def click_resp():
    """菜单点击类型回复"""
    response = wechat.response_text("""该功能正在开发中...""")
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


def return_to_pic(pic_key):
    if pic_key is None:
        return ""
    # app.config['CITY_PIC_KEY'][pic_key.decode('utf-8')]
    return wechat.response_image(pic_key)


def return_to_video(video_key):
    if video_key is None:
        return ""
    return wechat.response_video(video_key)


def return_to_voice(voice_key):
    if voice_key is None:
        return ""
    return wechat.response_voice(voice_key)


def return_to_text(text_key):
    if text_key is None:
        return ""
    return wechat.response_text(text_key)
