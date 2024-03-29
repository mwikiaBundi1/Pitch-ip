import os

class Config:
    # SECRET_KEY = 'madash'
    SECRET_KEY =  os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin:malkie@localhost/karuku'
    UPLOADED_PHOTOS_DEST = 'app/static/photo'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME =  os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SUBJECT_PREFIX = 'pitches'
    SENDER_EMAIL = 'mwikiam@gmail.com'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    SQLALCHEMY_TRACK_MODIFICATIONS=True 

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI =  'postgresql+psycopg2://martin:malkie@localhost/karuku'
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://martin:malkie@localhost/karuku'

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig

    }