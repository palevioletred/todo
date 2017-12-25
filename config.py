# encoding=utf-8
from env import ENV


class Config(object):
    pass


class DevelopmentConfig(Config):
    MONGODB_SETTINGS = {
        'db': 'test',
        'host': 'localhost',
        'port': 27017
    }


class ProductConfig(Config):
    pass


config = {
    'product': ProductConfig,
    'development': DevelopmentConfig
}.get(ENV, DevelopmentConfig)
