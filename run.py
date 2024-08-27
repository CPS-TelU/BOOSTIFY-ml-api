from flask import Flask
from app.config import Config
from app.routes.main_routes import main_routes

app = Flask(__name__)
app.config.from_object(Config)

# Register the blueprint
app.register_blueprint(main_routes)

if __name__ == "__main__":
    app.run(debug=True)
