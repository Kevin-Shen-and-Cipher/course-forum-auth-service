from datetime import datetime

import jwt
from utils import config


def encode_jwt(department, identify, exp):
    payload = {'department': department, 'identify': identify, 'exp': exp}
    secret_key = config.get_secret_key()

    jwt_token = jwt.encode(payload, secret_key, algorithm='HS256')
    return jwt_token