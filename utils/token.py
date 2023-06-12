import jwt
from jwt import ExpiredSignatureError

from utils import config


def encode_jwt(department, identify, exp):
    payload = {'department': department, 'identify': identify, 'exp': exp}
    secret_key = config.get_secret_key()

    jwt_token = jwt.encode(payload, secret_key, algorithm='HS256')
    return jwt_token


def decode_jwt(jwt_token):
    data = {}
    try:
        secret_key = config.get_secret_key()
        decoded_token = jwt.decode(jwt_token, secret_key, algorithms=["HS256"])
        data = {'identify': decoded_token['identify']}

        return 200, data
    except ExpiredSignatureError as error:
        print("jwt expired:", error)
        return 403, data
    except Exception as error:
        print("decode jwt error:", error)
        return 500, data
