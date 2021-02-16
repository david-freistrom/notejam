import os
import logging

class Config(object):
    TESTING = True
    WTF_CSRF_ENABLED = False

    # Logging Configurtion
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = '/dev/stdout'
    LOGGING_LEVEL = logging.DEBUG

    CSRF_SESSION_KEY = 'notejam-flask-secret-key'
    SECRET_KEY = 'notejam-flask-secret-key'