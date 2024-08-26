from flask import Blueprint, jsonify

# Create a blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Flask API!"
    })
