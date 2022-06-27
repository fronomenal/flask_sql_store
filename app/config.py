import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY", "pwrd-key-secret")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../store.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdCon(Config):
    FLASK_ENV = 'production'
    DEBUG = False


class StageCon(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevCon(Config):
    FLASK_ENV = 'development'
    DEVELOPMENT = True
    DEBUG = True


# class TestCon(Config):
#     TESTING = True