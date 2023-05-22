from flask import Flask, request, jsonify
from utils import auth_service,config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    username = auth['username']
    password = auth['password']

    http_code, data = auth_service.login(username, password)

    return jsonify(data), http_code

@app.route('/verify', methods=['POST'])
def tokens_verify():
    auth = request.get_json()
    jwt = auth['token']

    http_code, data = auth_service.verify(jwt)

    return jsonify(data), http_code

if __name__ == "__main__":
    IP = config.get_ip()
    PORT = config.get_port()
    app.run(debug=True, host=IP, port=PORT)