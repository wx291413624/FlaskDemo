#!/usr/bin/env python
# -*- coding: utf-8 -*-
from celery.schedules import crontab

DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql://root:Kiretyo1521@47.95.235.183:3306/guns?charset=utf8mb4"
# SQLALCHEMY_DATABASE_URI = "mysql://debian-sys-maint:PmOL3zdw6WErzZ7a@127.0.0.1:3306/TEST?charset=utf8mb4"

MYSQL_CURSORCLASS = 'DictCursor'

MONGO_URI = "mongodb://39.96.73.116:27017/gas"
# MONGO_URI = "mongodb://localhost:27017/gas"

REDIS_HOST = '39.96.73.116'

# 微信公众平台配置
APP_ID = "wx2f772ca355796adb"
APP_SECRET = "c454b124437d7f656a529911eda93cba"
TOKEN = "nengshuguanwei"
EncodingAESKey = "6gzMRGule1gjR4fNHTMoIx7XW9bxClzSw4TdVYWDHvh"

# celery 配置
CELERY_BROKER_URL = 'redis://39.96.73.116:6379/1'
CELERY_RESULT_BACKEND = 'redis://39.96.73.116:6379/2'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYBEAT_SCHEDULE = {
    'every-1-hour': {
        'task': 'access_token.update',
        'schedule': crontab(minute=0, hour='*/1')
    }
}

MENU_SETTING = {
    "button": [
        {
            "type": "view",
            "name": "跑腿侠申请",
            "url": "http://www.baidu.com/"
        },
        {
            "type": "view",
            "name": "任务广场",
            "url": "http://www.baidu.com/"
        },
        {
            "type": "view",
            "name": "我的账户",
            "url": "http://www.baidu.com/"
        }
    ]
}

MENU_TEST_CLICK = {
    "button": [
        {
            "type": "click",
            "name": "跑腿侠申请",
            "key": "TEST_CLICK"
        },
        {
            "type": "click",
            "name": "任务广场",
            "key": "TEST_CLICK"
        },
        {
            "type": "click",
            "name": "我的账户",
            "key": "TEST_CLICK"
        }
    ]
}

CITY_PIC_KEY = {
    u'重庆': u'6xbcktgL5KVQDsNjXNrAxden-GUgfV_CpmlwnhknI4A',
    u'北京': u'6xbcktgL5KVQDsNjXNrAxTwHdpMjnE6I_ybyHByFPXo',
    u'西安': u'6xbcktgL5KVQDsNjXNrAxc-ySgKiQLSurS9OhT6RpbU'
}
