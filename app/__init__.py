from flask import Flask
from app.extensions import db
from app.routes.routes import attendance_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    
    app.register_blueprint(attendance_bp)
    
    return app
