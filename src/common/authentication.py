from functools import wraps

import jwt
from flask import request, jsonify
from werkzeug.security import safe_str_cmp

from src.model import User


def authenticate(username, password):
    users = User()
    try:
        user = User.get(User.username == username)
        print(user.password)
        if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
            return user
        return None
    except:
        return None


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
        token = token[7:len(token)]
        print(token)
        try:

            request.user = jwt.decode(token, key='super-secret')
        except Exception as e:
            print(e)
            return jsonify({'message': 'token is invalid!'}), 403

        return f(*args, **kwargs)

    return decorated


def is_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        print(request.user)
        try:
            if request.user['role'] == 1:
                pass
            else:
                return jsonify({'message': 'deny!'}), 403

        except Exception as e:
            print(e)
            return jsonify({'message': 'deny'}), 405

        return f(*args, **kwargs)

    return decorated
