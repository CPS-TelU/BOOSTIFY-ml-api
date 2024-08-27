from flask import Blueprint, request, jsonify, current_app
import requests

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/add-attendance', methods=['POST'])
def add_attendance():
    data = request.json
    name = data.get('name')
    assistant_code = data.get('assistant_code')

    if not name or not assistant_code:
        return jsonify({"error": "Name and Assistant Code are required"}), 400

    # Correct Supabase REST API URL
    supabase_url = current_app.config['SUPABASE_URL']
    supabase_api_key = current_app.config['SUPABASE_KEY']
    table_name = "attendances"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {supabase_api_key}"
    }

    data_to_insert = {
        "name": name,
        "assistant_code": assistant_code,
    }

    try:
        response = requests.post(
            f"{supabase_url}/rest/v1/{table_name}",
            headers=headers,
            json=data_to_insert
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        current_app.logger.error(f"Failed to connect to Supabase: {e}")
        return jsonify({"error": "Failed to connect to Supabase", "details": str(e)}), 500

    if response.status_code == 201:
        return jsonify({"message": "Attendance recorded successfully"}), 201
    else:
        return jsonify({"error": "Failed to record attendance", "details": response.json()}), response.status_code
