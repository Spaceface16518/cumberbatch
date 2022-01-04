import os

DATABASE_URI = os.getenv('DATABASE_URI') or 'sqlite:///:memory:'
SECRET_KEY = os.getenv('SECRET_KEY') or 'development key'
