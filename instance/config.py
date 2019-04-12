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
APP_ID = ""
APP_SECRET = ""
TOKEN = ""
EncodingAESKey = ""

# celery 配置
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/1'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYBEAT_SCHEDULE = {
    'every-1-minute': {
        'task': 'access_token.update',
        'schedule': crontab(minute='*/1')
    }
}
