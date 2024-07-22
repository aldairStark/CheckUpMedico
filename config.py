import os

class Config(object):
    SECRET_KEY =''

class DecelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ''
