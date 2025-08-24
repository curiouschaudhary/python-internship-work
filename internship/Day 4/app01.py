from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage (dictionary)
users = {}

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({user_id: user}), 200
    return jsonify({'error': 'User not found'}), 404

# POST - create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = data.get("id")
    name = data.get("name")
    
    if user_id is None or name is None:
        return jsonify({'error': 'Missing id or name'}), 400

    if user_id in users:
        return jsonify({'error': 'User already exists'}), 409

    users[user_id] = {"name": name}
    return jsonify({'message': 'User created successfully'}), 201

# PUT - update existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404

    data = request.json
    name = data.get("name")
    if name:
        users[user_id]["name"] = name
        return jsonify({'message': 'User updated successfully'}), 200
    else:
        return jsonify({'error': 'No data to update'}), 400

# DELETE - remove a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({'message': 'User deleted successfully'}), 200
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
