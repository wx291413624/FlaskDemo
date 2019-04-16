# coding=utf-8
import uuid

from main import app, request, jsonify
import oss2

ALLOWED_EXTENSIONS = {'png', 'jpg', 'JPG', 'PNG'}
pic_url = "ns-collectgas.oss-cn-beijing.aliyuncs.com"


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


auth = oss2.Auth('LTAIE7oNUyJ19o3B', '4KPpCAZZTqfs4V1Ouro53z8fJOFnx6')
bucket = oss2.Bucket(auth, 'oss-cn-beijing-internal.aliyuncs.com', 'ns-collectgas')


@app.route("/pic", methods=['GET', 'POST'])
def pic():
    app.logger.info('----------pic upload start-----------')
    uid = uuid.uuid1()
    fs = request.files.getlist('file')
    pic_list = []
    for f in fs:
        name = str.replace(str(uid), '-', '')
        bucket.put_object(name, f)
        pic_list.append(pic_url + "/" + name + "?x-oss-process=image/resize,h_100")
    app.logger.info('----------pic upload success-----------')
    return jsonify(pic_list)
