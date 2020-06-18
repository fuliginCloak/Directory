import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '930058ed0dbc618046eb924ac81ad85d'