from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

from . import config
from . import models
from . import views
from . import forms

import logging

mail = Mail()

def create_app():
    """ Initiation function to create the flask application """
    app = Flask(__name__, instance_relative_config=True)
    
    with app.app_context():

        config.init_app(app)
        models.init_app(app)

        mail.init_app(app)

        views.init_app(app)
        forms.init_app(app)

        app.logger.info("fdsada")

    return app

