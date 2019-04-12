# -*- coding: utf-8 -*-


from __future__ import unicode_literals

import json
import requests


class wechat_login(object):

    def __init__(self, app_id, app_secret):
        self.sess = requests.Session()
        self.app_id = app_id
        self.app_secret = app_secret

    def _get(self, url, params):
        resp = self.sess.get(url, params=params)
        data = json.loads(resp.content.decode("utf-8"))
        if data['errcode']:
            msg = "%(errcode)d %(errmsg)s" % data
            raise Exception(msg)
        return data

    def access_token(self, code):
        """
        获取令牌
        """
        url = "https://api.weixin.qq.com/sns/oauth2/access_token"
        args = dict()
        args.setdefault("appid", self.app_id)
        args.setdefault("secret", self.app_secret)
        args.setdefault("code", code)
        args.setdefault("grant_type", "authorization_code")
        return self._get(url, args)

    def user_info(self, access_token, openid):
        """
        获取用户信息
        """
        url = "https://api.weixin.qq.com/sns/userinfo"
        args = dict()
        args.setdefault("access_token", access_token)
        args.setdefault("openid", openid)
        args.setdefault("lang", "zh_CN")
        return self._get(url, args)
