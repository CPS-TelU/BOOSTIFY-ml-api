from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration from config.py
    app.config.from_object('config')

    # Register routes
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
