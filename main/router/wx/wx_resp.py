#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    response = wechat.response_text("""欢迎您进圈来了就别想空着手出去啦

欢迎关注  加油同时  不给你钱包揣鼓点儿都不是我们风格
轻松做任务  免费得现金、加油券🧧

回复【地区关键字（如：北京）】加入微信群，更多赚钱小任务等你来领

点击开始赚钱：http://cirhu4gwph612vcj.mikecrm.com/FiEBphp
附赠一本赚钱秘籍：https://m.eqxiu.com/s/hxhWrFzw

跑腿侠江湖召集令，等你跑出省油赚钱一片天！""")
    app.logger.info(response)
    return response


@set_msg_type('text')
def text_resp():
    """文本类型回复"""
    message.content = message.content.replace(u'　', ' ')
    message.content = message.content.lstrip()
    list = redis.hgetall('keyword:all')
    response = 'success'
    for key_word in list:
        if key_word == message.content:
            if list[key_word] == '1':
                response = return_to_pic(key_word)
            elif list[key_word] == '2':
                response = return_to_video(key_word)
            elif list[key_word] == '3':
                response = return_to_voice(key_word)
            else:
                response = ''
            break
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
    redis_media_id = redis.get('text:back:' + pic_key)
    if redis_media_id is None:
        return ""
    # app.config['CITY_PIC_KEY'][pic_key.decode('utf-8')]
    return wechat.response_image(redis_media_id)


def return_to_video(video_key):
    redis_media_id = redis.get('video:back:' + video_key)
    if redis_media_id is None:
        return ""
    return wechat.response_video(redis_media_id)


def return_to_voice(voice_key):
    redis_media_id = redis.get('voice:back:' + voice_key)
    if redis_media_id is None:
        return ""
    return wechat.response_voice(redis_media_id)
