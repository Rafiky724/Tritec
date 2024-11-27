import os
from dotenv import load_dotenv
from flask import Flask
from app.routes.routesData import bp
from config import Config

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY')
    
    app.config.from_object(Config)
    
    # Registrar Blueprints
    app.register_blueprint(bp)
    
    return app
