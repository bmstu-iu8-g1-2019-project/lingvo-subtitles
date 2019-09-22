from flask import Flask, request, jsonify
from subtitles import controller

app = Flask(__name__)


@app.route('/')
def root_view():
    return 'subtitle-backend API version indev'


@app.route('/search')
def search_view():
    ctrl = controller.Controller()

    request_query = request.form['query']

    raw_response = ctrl.search_by_name_get_first_n(request_query)

    return jsonify(raw_response)


if __name__ == '__main__':
    app.run(debug=True)
