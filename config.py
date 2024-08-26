import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    # Add more configuration variables as needed

# Load configurations from Config class
config = Config()
