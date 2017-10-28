import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Global configuration settings"""
    SECRET_KEY = 'You cannot hack this site fool'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    @staticmethod
    def init_app(app):
        pass

class Development(Config):
    """Settings used for development"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql:///yummy_recipes'
    

class Testing(Config):
    """Settings used for testing"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql:///yummy_recipes'

class Production(Config):
    """Settings used for production"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql:///yummy_recipes'

config = {
    'development': Development,
    'testing': Testing,
    'production': Production,
    'default': Development
}
