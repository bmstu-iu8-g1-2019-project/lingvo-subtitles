from werkzeug.security import generate_password_hash, check_password_hash  # Default hash set to pbkdf2:sha256

from app import auth

users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye")
}


@auth.error_handler
def error_handler():
    return {"id": "401", "message": "Unauthorized"}, 401


@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False
