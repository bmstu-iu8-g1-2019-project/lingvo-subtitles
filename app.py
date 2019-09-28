import os
import sys

from flask import Flask, request, jsonify
from subtitles import controller

app = Flask(__name__)

if 'YANDEX_TRANSLATE_API_KEY' in os.environ:
    yandex_translate_api_key = os.environ['YANDEX_TRANSLATE_API_KEY']
else:
    print('You have to provide Yandex Translate Api key, set YANDEX_TRANSLATE_API_KEY and restart')
    sys.exit(1)

ctrl = controller.Controller(yandex_translate_api_key)


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
