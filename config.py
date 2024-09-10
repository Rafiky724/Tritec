import os

class Config:
    TEMPLATES_FOLDER = os.path.join(os.path.dirname(__file__), 'app/templates')
    STATIC_FOLDER = os.path.join(os.path.dirname(__file__), 'app/static')
