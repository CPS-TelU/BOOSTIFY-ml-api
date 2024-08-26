import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')  # URI PostgreSQL Supabase Anda
    SQLALCHEMY_TRACK_MODIFICATIONS = False
