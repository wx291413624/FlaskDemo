# coding=utf-8
import hashlib
from functools import wraps

from flask import request

from main import app, redis


def url_param(func):
    @wraps(func)
    def test(*args, **kwargs):
        try:
            if request.method == 'POST':
                tm = request.form.get('tm')
                strs = request.form.get('str')
                m_key = request.form.get('mkey')
            else:
                tm = request.args.get('tm')
                strs = request.args.get('str')
                m_key = request.args.get('mkey')
            mkey = tm + "" + strs
            # rst = redis.lock("request:" + mkey, 600)
            if hashlib.md5(mkey).hexdigest() == m_key:
                app.logger.info("----signature success----")
                return func(*args, **kwargs)
            else:
                return "signature failed"
        except Exception as e:
            app.logger.info("---signature error----")
            return 'signature error'

    return test


def phonelist(phone):
    if phone:
        list = phone[3:7]
        newphone = phone.replace(list, '****')
        return newphone
    else:
        return None
