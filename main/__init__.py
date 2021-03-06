#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
from flask_cors import *
from flask_pymongo import PyMongo
from flask_restplus import Resource, Api
from redis import Redis
import flask_excel as excel
from main.plugins.queue import make_celery

app = Flask(__name__, instance_relative_config=True, template_folder='../templates', static_folder='../static')
api = Api(app, version='1.0', title='GAS API', description='A simple gas_MVC API', )

# 加载配置
app.config.from_pyfile('config.py')
CORS(app, supports_credentials=True)
excel.init_excel(app)
# 初始第三方库
mongo = PyMongo(app)
wx_mongo = PyMongo(app, uri=app.config['WX_MONGO_URI'])
celery = make_celery(app)
redis = Redis(decode_responses=True, host=app.config['REDIS_HOST'], password=app.config['REDIS_PASSWORD'], db=0)

# 记录日志
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
handler.setLevel(logging.WARNING)
app.logger.addHandler(handler)

# 路由
from .router.gas import *
from .router.ding_talk import *
from .router.pic import *
from .router.plus import *
from .router.wx.wx_cron import *
from .router.lazy.material import *
from .router.lazy.keyword import *
from .router.lazy.follow import *
from .router.lazy.gas import *
from .router.lazy.login_sys import *
