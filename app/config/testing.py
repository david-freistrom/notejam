import os
import logging

class Config(object):
    TESTING = True
    WTF_CSRF_ENABLED = False

    POSTGRES_URL = os.getenv("POSTGRES_URL", '10.44.0.3:5432')
    POSTGRES_USER = os.getenv("POSTGRES_USER", 'notejam')
    POSTGRES_PW = os.getenv("POSTGRES_PW", 'password1234!')
    POSTGRES_DB = os.getenv("POSTGRES_DB", 'notejam-db')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Logging Configurtion
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'notejam.log'
    LOGGING_LEVEL = logging.DEBUG

    CSRF_SESSION_KEY = 'notejam-flask-secret-key'
    SECRET_KEY = 'notejam-flask-secret-key'

    # Mailer Configuration
    MAIL_SERVER = 'mail.freistrom.io'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv("MAIL_USER", 'notejam@freistrom.io')
    MAIL_PASSWORD = os.getenv("MAIL_PW", 'mZ-Rj7A3Vj@-')
    MAIL_DEFAULT_SENDER = 'notejam@freistrom.io'
    