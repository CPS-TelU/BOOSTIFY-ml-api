# app/routes/main_routes.py
from flask import Blueprint, jsonify

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask app!"})
