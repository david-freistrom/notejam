import os
import logging

class Config(object):
    DEBUG = False
    
    POSTGRES_URL = os.getenv("POSTGRES_URL", 'localhost:5432')
    POSTGRES_USER = os.getenv("POSTGRES_USER", 'notejam')
    POSTGRES_PW = os.getenv("POSTGRES_PW", '')
    POSTGRES_DB = os.getenv("POSTGRES_DB", 'notejam-db')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SECRET_KEY = 'OVERWRITE_ME' 
    
    # Logging Configurtion
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = '/dev/stdout'
    LOGGING_LEVEL = logging.DEBUG
    
    SECURITY_PASSWORD_SALT = 'CHANGE_ME'

    # Mailer Configuration
    MAIL_SERVER = 'mail.freistrom.io'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv("MAIL_USER", 'notejam@freistrom.io')
    MAIL_PASSWORD = os.getenv("MAIL_PW", 'mZ-Rj7A3Vj@-')
    MAIL_DEFAULT_SENDER = 'notejam@freistrom.io'
    