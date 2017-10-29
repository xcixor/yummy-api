"""The purpose of this constructor is to set up the api
by importing the necessary modules for the app to run
Methods:
    create_app: Serves as the app factory
"""
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app(configuration):
    """It initializes the application"""

    app = Flask(__name__)
    app.config.from_object(config[configuration])
    config[configuration].init_app(app)

    db.init_app(app)

    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint)
    
    return app


