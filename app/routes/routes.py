from flask import Blueprint
from app.controllers.attendance_controller import post_attendance

attendance_bp = Blueprint('attendance_bp', __name__)

attendance_bp.route('/attendance', methods=['POST'])(post_attendance)
