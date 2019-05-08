# coding=utf-8

from main import app


@app.errorhandler(404)
def page_not_found(error):
    return "not found!", 200


@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.error('Unhandled Exception: %s', (error))
    return error, 200
