import os
from pathlib import Path
import logging

class Config(object):
    DEBUG = False
    TESTING = False
    
    SECRET_KEY = 'notejam-flask-secret-key'
    WTF_CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'notejam-flask-secret-key'

    basedir = Path(__file__).parent
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///' + os.path.join(basedir, 'notejam.db'))

    # Logging Configurtion
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'notejam.log'
    LOGGING_LEVEL = logging.DEBUG

    # Mailer Configuration
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 1025
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_DEFAULT_SENDER = 'notejam@localhost'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

    POSTGRES_URL = os.getenv("POSTGRES_URL", 'localhost:5432')
    POSTGRES_USER = os.getenv("POSTGRES_USER", 'notejam')
    POSTGRES_PW = os.getenv("POSTGRES_PW", 'password1234!')
    POSTGRES_DB = os.getenv("POSTGRES_DB", 'notejam-db')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class ProductionConfig(Config):
    
    POSTGRES_URL = os.getenv("POSTGRES_URL", 'localhost:5432')
    POSTGRES_USER = os.getenv("POSTGRES_USER", 'notejam')
    POSTGRES_PW = os.getenv("POSTGRES_PW", '')
    POSTGRES_DB = os.getenv("POSTGRES_DB", 'notejam-db')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
        
    # Mailer Configuration
    MAIL_SERVER = 'mail.freistrom.io'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv("MAIL_USER", 'notejam@freistrom.io')
    MAIL_PASSWORD = os.getenv("MAIL_PW", 'mZ-Rj7A3Vj@-')
    MAIL_DEFAULT_SENDER = 'notejam@freistrom.io'

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False