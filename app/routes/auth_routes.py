# app/routes/auth_routes.py
from flask import Blueprint, request, jsonify

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Dummy check
    if username == 'user' and password == 'password':
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Dummy registration logic
    return jsonify({"message": "Registration successful"}), 201
