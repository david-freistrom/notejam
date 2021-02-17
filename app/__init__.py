from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager

from . import config
from . import models
from . import views
from . import forms

import logging


mail = Mail()
app = Flask(__name__, instance_relative_config=True)
login_manager = LoginManager()
login_manager.login_view = "signin"
login_manager.init_app(app)

def create_app():
    """ Initiation function to create the flask application """
    with app.app_context():
        config.init_app(app)
        models.init_app(app)

        mail.init_app(app)

        views.init_app(app)
        forms.init_app(app)

    return app