import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Global configuration settings"""
    SECRET_KEY = 'You cannot hack this site fool'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    password = 'pN75216895#'
    username = 'xcixor'
    database = 'yummy_recipes'


    @staticmethod
    def init_app(app):
        pass

class Development(Config):
    """Settings used for development"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://xcixor:pN75216895#@localhost/yummy_recipes'


class Testing(Config):
    """Settings used for testing"""
    TESTING = True

class Production(Config):
    """Settings used for production"""
    DEBUG = False

config = {
    'development': Development,
    'testing': Testing,
    'production': Production,

    'default': Development
}
