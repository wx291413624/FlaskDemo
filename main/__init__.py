#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
from flask_cors import *
from flask_pymongo import PyMongo
from flask_restplus import Resource, Api
from redis import Redis

from main.plugins.queue import make_celery

app = Flask(__name__, instance_relative_config=True, template_folder='../templates', static_folder='../static')
api = Api(app, version='1.0', title='GAS API', description='A simple gas_MVC API', )

# 加载配置
app.config.from_pyfile('config.py')
CORS(app, supports_credentials=True)

# 初始第三方库
mongo = PyMongo(app)
celery = make_celery(app)
redis = Redis(host=app.config['REDIS_HOST'])

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
