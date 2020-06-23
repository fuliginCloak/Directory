import os
basedir= os.path.abspath(os.path.dirname(__file__))



class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '930058ed0dbc618046eb924ac81ad85d'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLACHEMY_TRACK_MODIFICATIONS = False


