from flask import Flask, request, jsonify
from subtitles import controller

app = Flask(__name__)
ctrl = controller.Controller()


@app.route('/')
def root_view():
    return 'subtitle-backend API version indev'


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
    app.run()
