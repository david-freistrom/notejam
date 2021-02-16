import os
import logging

class Config(object):
    DEBUG = False
    TESTING = False 

    # Database Configuration for PostgreSQL
    POSTGRES_URL = os.getenv("POSTGRES_URL", 'localhost:5432')
    POSTGRES_USER = os.getenv("POSTGRES_USER", 'notejam')
    POSTGRES_PW = os.getenv("POSTGRES_PW", 'password1234!')
    POSTGRES_DB = os.getenv("POSTGRES_DB", 'notejam-db')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    WTF_CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'notejam-flask-secret-key'
    SECRET_KEY = 'notejam-flask-secret-key'
    
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