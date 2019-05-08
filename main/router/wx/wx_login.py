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
        resp = requests.get(url, params=params)
        data = json.loads(resp.content.decode("utf-8"))
        if data['errcode']:
            msg = "%(errcode)d %(errmsg)s" % data
            raise Exception(msg)
        return data

    def _post(self, url, params):
        resp = requests.post(url, json=params)
        data = json.loads(resp.content.decode("utf-8"))
        if data['errcode']:
            msg = "%(errcode)d %(errmsg)s" % data
            raise Exception(msg)
        return data

    def _post_upload_file(self, url, files):
        resp = self.sess.post(url, files=files)
        data = json.loads(resp.content.decode("utf-8"))
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

    def upload_file(self, access_token, files, media_type):
        """上传永久素材 """
        files = {'media': (files.filename, files, files.filename.split('.')[-1].lower()), 'filename': files.filename}
        url = "https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=%s&type=%s" % (
            access_token, media_type)
        return self._post_upload_file(url, files)

    def del_file(self, access_token, media_id):
        """删除永久素材"""
        url = 'https://api.weixin.qq.com/cgi-bin/material/del_material?access_token=%s' % access_token
        params = dict()
        params.setdefault('media_id', media_id)
        return self._post(url, params)
