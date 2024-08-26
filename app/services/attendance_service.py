from app.extensions import db
from app.models.attendance import Attendance

def create_attendance(assisstant_code, name, time):
    new_attendance = Attendance(
        assisstant_code=assisstant_code,
        name=name,
        time=time
    )
    db.session.add(new_attendance)
    db.session.commit()
    return new_attendance
