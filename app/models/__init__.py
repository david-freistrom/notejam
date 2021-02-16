from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
  print("app.models.__init__.init_app()")
  db.init_app(app)
  db.create_all()

from .users import User
from .pads import Pad
from .notes import Note

__all__ = [User, Pad, Note]