# coding=utf-8
from main import celery
from main.router.wx.wx_utils import update_wechat_token


@celery.task(name='access_token.update')
def update_access_token():
    """定时更新微信 access_token，写入缓存"""
    print """test celery wechat test"""
    # update_wechat_token()
