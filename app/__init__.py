from flask import Flask
from .routes.main_routes import main_routes
from .routes.auth_routes import auth_routes
from .config import Config  # Update the import to reflect the new location

def create_app():
    app = Flask(__name__)

    # Load configuration from Config class
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(main_routes)
    app.register_blueprint(auth_routes)

    return app
