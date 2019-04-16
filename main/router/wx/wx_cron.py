# coding=utf-8
from main import celery, app
from main.router.wx.wx_utils import update_wechat_token


@celery.task(name='access_token.update')
def update_access_token():
    """定时更新微信 access_token，写入缓存"""
    app.logger.info('------wechat_access_token_update---------')
    update_wechat_token()
