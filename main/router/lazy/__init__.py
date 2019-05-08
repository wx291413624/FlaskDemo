# coding=utf-8
import datetime
from functools import wraps

from flask import session, render_template

from main import app, request


def check_login(func):
    @wraps(func)
    def test(*args, **kwargs):
        try:
            if session['token'] is None:
                return render_template('index.html')
            return func(*args, **kwargs)
        except Exception as e:
            app.logger.info(e)
            return render_template('index.html')

    return test


@app.route("/index", methods=['GET'])
def ex_index():
    return render_template('index.html')


@app.route("/ex/logout", methods=['GET'])
def ex_logout():
    session.clear()
    return render_template('index.html')


@app.route("/ex/login", methods=['POST'])
def ex_login():
    acc = request.form.get('acc')
    pwd = request.form.get('pwd')
    if acc == "admin" and pwd == "admin":
        session['token'] = {'acc': acc, 'pwd': pwd}
        return render_template('home.html', welcome='WELCOME', time=str(datetime.date.today()), error='登陆成功')
    return render_template('index.html', desc=u'登录失败...请重新登录', )


@app.route("/home", methods=['GET'])
@check_login
def ex_home():
    return render_template('home.html', welcome='WELCOME', time=str(datetime.date.today()))
