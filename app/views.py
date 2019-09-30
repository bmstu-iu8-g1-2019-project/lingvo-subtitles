import os

from flask import request, jsonify

from app import app
from app import controller

ctrl = controller.Controller(os.environ['YANDEX_TRANSLATE_API_KEY'])


@app.route('/')
def root_view():
    return 'lingvo API version indev'


@app.route('/search')
def search_view():
    request_query = request.form['query']

    raw_response = ctrl.search_by_name_get_first_n(request_query)

    return jsonify(raw_response)


@app.route('/parse')
def parse_view():
    request_query = request.form['query']

    return jsonify(ctrl.get_learning_mode_data(request_query))
