from functools import wraps
from werkzeug.security import safe_str_cmp
from src1.models.user import User
import jwt
from flask import request, jsonify


def authenticate(username, password):
    users = User()
    user = users.get_user_by_username(username)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    return user_id


def create_token(payload):
    return jwt.encode(payload, key='super-secret')


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'token is missing !'}), 401
        try:
            pass
        except:
            return jsonify({'message': 'token is invalid!'}), 403

        return f(*args, **kwargs)

    return decorated
