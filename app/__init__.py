# app/__init__.py
from flask import Flask
from .routes.main_routes import main_routes
from .routes.auth_routes import auth_routes

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('config.Config')  # Adjust as needed

    # Register blueprints
    app.register_blueprint(main_routes)
    app.register_blueprint(auth_routes, url_prefix='/auth')

    # Initialize other extensions (if any)
    # db.init_app(app)
    # login_manager.init_app(app)

    return app
