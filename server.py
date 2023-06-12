from flask import Flask, request, jsonify
from utils import auth_service, config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
_IP = config.get_ip()
_PORT = config.get_port()


@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    try:
        username = auth['username']
        password = auth['password']
        http_code, data = auth_service.login(username, password)
        return jsonify(data), http_code
    except KeyError as error:
        error_message = f"Missing required key: {error}"
        return jsonify({'error': error_message}), 400


@app.route('/verify', methods=['POST'])
def tokens_verify():
    auth = request.get_json()
    try:
        jwt = auth['token']
        http_code, data = auth_service.verify(jwt)
        return jsonify(data), http_code
    except KeyError as error:
        error_message = f"Missing required key: {error}"
        return jsonify({'error': error_message}), 400


if __name__ == "__main__":
    app.run(debug=True, host=_IP, port=_PORT)
