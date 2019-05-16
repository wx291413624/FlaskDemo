# coding=utf-8
from . import db


class SysUser(db.Model):
    __bind_key__ = 'sys'
    __tablename__ = 'sy_user'
    id = db.Column(db.INTEGER, primary_key=True)  # 主键
    account = db.Column(db.String(32), nullable=False)  # 帐号
    pwd = db.Column(db.String(32), nullable=False)  # 密码
    nick_name = db.Column(db.String(32), nullable=False)  # 姓名
    real_name = db.Column(db.String(32), nullable=True)  # 真实姓名
    sex = db.Column(db.SmallInteger, nullable=True)  # 性别
    head_img_key = db.Column(db.String(150), nullable=True)  # 头像
    states = db.Column(db.SmallInteger, nullable=False)  # 保留状态
    snacks_token = db.Column(db.String(32), nullable=False)  # 零时?标示token 登录使用

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update_commit(self):
        db.session.commit()
