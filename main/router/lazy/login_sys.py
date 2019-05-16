# coding=utf-8
from main.models.login_model import SysUser

from flask import session, render_template

from main import app, request
from main.router.lazy import check_login


@app.route("/sys", methods=['GET'])
@check_login
def ex_sys():
    return render_template('sys/sys.html', list=find_all())


def find_all():
    return SysUser.query.order_by(SysUser.id.desc()).all()


@app.route("/sys/del", methods=['POST'])
@check_login
def ex_sys_del():
    id = request.form.get('id')
    us = SysUser.query.filter_by(id=id).first()
    us.states = 1
    us.update_commit()
    return render_template('sys/sys.html', error='修改成功', list=find_all())


@app.route("/sys/ins", methods=['POST'])
@check_login
def ex_sys_insert():
    account = request.form.get('account')
    pwd = request.form.get('pwd')
    name = request.form.get('name')
    sex = request.form.get('sex')
    SysUser(account=account, pwd=pwd, nick_name=name, sex=sex, states=0).save()
    return render_template('sys/sys.html', error="success", list=find_all())
