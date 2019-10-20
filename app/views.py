import os

from flask import request, jsonify, abort

from app import app, auth
from app import controller

ctrl = controller.Controller(os.environ['YANDEX_TRANSLATE_API_KEY'])


@app.errorhandler(400)
def error404_view(exception):
    return {"id": "400", "message": "Bad request"}


@app.errorhandler(401)
def error404_view(exception):
    return {"id": "401", "message": "Unauthorized"}


@app.errorhandler(403)
def error404_view(exception):
    return {"id": "403", "message": "Forbidden"}


@app.errorhandler(404)
def error404_view(exception):
    return {"id": "404", "message": "Not found"}


@app.errorhandler(500)
def error404_view(exception):
    return {"id": "500", "message": "Internal server error"}


@app.route('/')
def root_view():
    return 'lingvo API version indev'


@app.route('/register', methods=['POST'])
def register_view():
    registration_result = controller.register(request.form['email'], request.form['username'],
                                              request.form['hashed_password'])

    if registration_result == -1:
        abort(400)
    else:
        return jsonify({"user_id": str(registration_result)}), 201


@app.route('/search')
def search_view():
    request_query = request.form['query']

    raw_response = ctrl.search_by_name_get_first_n(request_query)

    return jsonify(raw_response)


@app.route('/parse')
@auth.login_required
def parse_view():
    request_query = request.form['query']

    return jsonify(ctrl.get_learning_mode_data(request_query))

from .models import auth
