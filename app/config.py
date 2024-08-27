import os
from supabase import create_client, Client

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJ5cXR6d2Fwa2xmcm5kdHpkZnNjIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyMzY5NDAyMywiZXhwIjoyMDM5MjcwMDIzfQ.j-7P5-TcAJatgjQR3VauhYgI8CteRCXAXz7QMPzwG60')
    SUPABASE_URL = os.getenv('SUPABASE_URL', 'https://byqtzwapklfrndtzdfsc.supabase.co')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJ5cXR6d2Fwa2xmcm5kdHpkZnNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjM2OTQwMjMsImV4cCI6MjAzOTI3MDAyM30.vSa9rZXsnUT-bdOk4Yxisdauubk6BCppqac2BccodjY')

def create_supabase_client():
    url = Config.SUPABASE_URL
    key = Config.SUPABASE_KEY
    return create_client(url, key)
