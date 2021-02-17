import os
from pathlib import Path
import logging
import pdb

class Config(object):
    DEBUG = False
    TESTING = False
    
    SECRET_KEY = 'notejam-flask-secret-key'
    WTF_CSRF_ENABLED = os.getenv('WTF_CSRF_ENABLED', True)
    CSRF_SESSION_KEY = 'notejam-flask-secret-key'

    # Logging Configurtion
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'notejam.log'
    LOGGING_LEVEL = logging.DEBUG

    POSTGRES_URL = os.getenv("POSTGRES_URL", 'localhost:5432')
    POSTGRES_USER = os.getenv("POSTGRES_USER", 'notejam')
    POSTGRES_PW = os.getenv("POSTGRES_PW", 'password1234!')
    POSTGRES_DB = os.getenv("POSTGRES_DB", 'notejam-db')

    # Mailer Configuration
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_DEFAULT_SENDER = 'notejam@localhost'
    MAIL_USERNAME = os.getenv("MAIL_USER", 'notejam@localhost')
    MAIL_PASSWORD = os.getenv("MAIL_PW", 'password1234!')


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    
class ProductionConfig(Config):        
    # Mailer Configuration
    MAIL_SERVER = 'mail.freistrom.io'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USE_SSL = True
    
class TestingConfig(Config):
    TESTING = True
    LOGGING_LEVEL = logging.DEBUG
    DEBUG = False

    MAIL_SERVER = 'mail.freistrom.io'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USE_SSL = True