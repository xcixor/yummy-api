import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    
    SECRET_KEY = 'You cannot hack this site fool'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class Development(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = postgresql://xcixor:pN75216895@hostname/database


class Testing(Config):
    TESTING = True

class Production(Config):
    DEBUG = False

config = {
    'development': Development,
    'testing': Testing,
    'production': Production,

    'default': Development
}
