import os

DATABASE_URL = os.getenv('DATABASE_URL') or 'sqlite:///:memory:'
SECRET_KEY = os.getenv('SECRET_KEY') or 'development key'
