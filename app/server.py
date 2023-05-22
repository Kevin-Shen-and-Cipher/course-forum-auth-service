from flask import Flask, request, jsonify
from utils import auth_service,config

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    username = auth.username
    password = auth.password

    http_code, data = auth_service.login(username, password)

    return http_code, jsonify(data)

@app.route('/verify', methods=['POST'])
def tokens_verify():
    auth = request.get_json()
    jwt = auth.token

    http_code, data = auth_service.verify(jwt)

    return http_code, jsonify(data)

if __name__ == "__main__":
    IP = config.get_ip()
    PORT = config.get_port()
    app.run(debug=True, host=IP, port=PORT)