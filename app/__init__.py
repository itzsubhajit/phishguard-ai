import os
from flask import Flask
from config import config

def create_app(config_name='development'):
    # Calculate root of the project (one level up from this app/ folder)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_dir = os.path.join(project_root, 'static')
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    app.config.from_object(config[config_name])
    from app.routes.detection import detection_bp
    app.register_blueprint(detection_bp)
    
    return app
