from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 模拟用户存储
users = []

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    # 检查用户是否已存在
    if any(user['username'] == username for user in users):
        return jsonify({'message': 'Username already exists'}), 400

    # 保存用户
    users.append({'username': username, 'password': password})
    return jsonify({'message': 'User registered successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)