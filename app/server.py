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


if __name__ == "__main__":
    IP = config.get_ip()
    app.run(debug=True, host=IP, port=5000)