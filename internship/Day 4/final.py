from flask import Flask, request, jsonify
import json
import os
import re

app = Flask(__name__)
DATA_FILE = 'data.json'

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as file:
        users = json.load(file)
        users = {int(k): v for k, v in users.items()}
else:
    users = {}

def save_users():
    with open(DATA_FILE, 'w') as file:
        json.dump(users, file, indent=4)

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET a single user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({user_id: user}), 200
    return jsonify({'error': 'User not found'}), 404

# POST - create new user (now with phone)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    age = data.get("age")
    phone = data.get("phone")  # NEW FIELD

    if not name or not email or not age:
        return jsonify({'error': 'Missing name, email or age'}), 400
    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email format'}), 400
    if not isinstance(age, int):
        return jsonify({'error': 'Age must be an integer'}), 400

    user_id = max(users.keys(), default=0) + 1
    users[user_id] = {"name": name, "email": email, "age": age, "phone": phone}
    save_users()
    return jsonify({'message': 'User created', 'user_id': user_id}), 201

# PUT - update user (now with phone)
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404

    data = request.json
    if "name" in data:
        users[user_id]["name"] = data["name"]
    if "email" in data:
        if not is_valid_email(data["email"]):
            return jsonify({'error': 'Invalid email format'}), 400
        users[user_id]["email"] = data["email"]
    if "age" in data:
        if not isinstance(data["age"], int):
            return jsonify({'error': 'Age must be an integer'}), 400
        users[user_id]["age"] = data["age"]
    if "phone" in data:  # NEW FIELD
        users[user_id]["phone"] = data["phone"]

    save_users()
    return jsonify({'message': 'User updated'}), 200

# DELETE user
@app.route('/')  # <-- Handles the root URL
def home():
    return """
    <h1>Welcome to the User API!</h1>
    <p>Try these endpoints:</p>
    <ul>
        <li><a href="/users">GET /users</a> → List all users</li>
        <li><a href="/count">GET /count</a> → Count users</li>
    </ul>
    """

# SEARCH by name
@app.route('/search', methods=['GET'])
def search_user():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Please provide a name to search'}), 400
    result = {uid: u for uid, u in users.items() if u['name'].lower() == name.lower()}
    return jsonify(result), 200

# NEW: Count total users
@app.route('/count', methods=['GET'])
def count_users():
    return jsonify({"total_users": len(users)}), 200

if __name__ == '__main__':
    app.run(debug=True)

# This code is a Flask application that provides a RESTful API for managing users.
# It supports creating, reading, updating, and deleting users, as well as searching by name

