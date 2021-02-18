import os, sys
import logging
from flask_dotenv import DotEnv
import pdb

def init_app(app):
  print("app.config.__init__.init_app()") 
  app.config.from_object("app.config.config." + os.getenv('FLASK_ENV', 'production').capitalize() + "Config")
  
  #DotEnv().init_app(app, verbose_mode=True)

  # Configure logging
  logging.basicConfig(level=app.config['LOGGING_LEVEL'],
                    format=app.config['LOGGING_FORMAT'],
                    handlers=[logging.StreamHandler()])  
