from flask import Flask
from app.routes.home_route import home_bp
from app.routes.problem_route import problem_bp
from config import Config

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    # Registrar Blueprints
    app.register_blueprint(home_bp, url_prefix='/')
    app.register_blueprint(problem_bp, url_prefix='/')
    
    return app
