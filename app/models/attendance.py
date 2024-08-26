from app.extensions import db
from datetime import datetime

class Attendance(db.Model):
    __tablename__ = 'Attendance'
    
    id = db.Column(db.Integer, primary_key=True)
    assisstant_code = db.Column(db.String(3), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Attendance {self.name}>'
