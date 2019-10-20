from flask import abort
from werkzeug.security import check_password_hash

from app import auth, db


@auth.error_handler
def error_handler():
    abort(401)


@auth.verify_password
def verify_password(username, password):
    user = db.auth.find_one({"username": username})

    if user is not None and check_password_hash(user["hashed_password"], password):
        return True

    return False
