from ..models import db
from sqlalchemy import Column, Integer, String

from werkzeug.security import (generate_password_hash, check_password_hash)
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)
    password = Column(String(100))

    @staticmethod
    def authenticate(email, password):
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            return user

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r>' % self.email

__all__ = [ User ]