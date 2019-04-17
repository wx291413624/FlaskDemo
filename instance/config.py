#!/usr/bin/env python
# -*- coding: utf-8 -*-
from celery.schedules import crontab

DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql://root:TcjdCKtFhrMI1fCK@rm-2ze228s38h786mys2xo.mysql.rds.aliyuncs.com:3306/TEST?charset=utf8mb4"
# SQLALCHEMY_DATABASE_URI = "mysql://debian-sys-maint:PmOL3zdw6WErzZ7a@127.0.0.1:3306/TEST?charset=utf8mb4"

MYSQL_CURSORCLASS = 'DictCursor'

MONGO_URI = "mongodb://39.96.73.116:27017/gas"
# MONGO_URI = "mongodb://localhost:27017/gas"

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
            "name": "主页",
            "url": "http://www.baidu.com/"
        },
        {
            "type": "view",
            "name": "任务",
            "url": "http://www.baidu.com/"
        },
        {
            "type": "view",
            "name": "个人",
            "url": "http://www.baidu.com/"
        }
    ]
}
