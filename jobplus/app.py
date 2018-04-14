from flask import Flask
from .models import db
from .config import configs
from .handlers import front, enterprise, job

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(front)
    app.register_blueprint(job)
    app.register_blueprint(enterprise)
    
