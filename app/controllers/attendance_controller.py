from flask import request, jsonify
from app.services.attendance_service import create_attendance

def post_attendance():
    data = request.get_json()
    
    assisstant_code = data.get('assisstant_code')
    name = data.get('name')
    time = data.get('time')
    
    if not all([assisstant_code, name, time]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    attendance = create_attendance(assisstant_code, name, time)
    return jsonify({'id': attendance.id}), 201
