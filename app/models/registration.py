from collections import Counter
from werkzeug.security import generate_password_hash

from app import db


def register_user(email, username, password):
    db.auth.drop()
    if db.auth.find_one({"username": username}) is not None:
        return -1
    if db.auth.find_one({"email": email}) is not None:
        return -1

    new_user = {
        "username": username,
        "email": email,
        "hashed_password": generate_password_hash(password),
        "words": Counter()
    }
    return db.auth.insert_one(new_user).inserted_id
