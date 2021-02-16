from ..models import db
from sqlalchemy import Column, Integer, String, ForeignKey

class Pad(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    user_id = Column(Integer, ForeignKey('user.id'))
    user = db.relationship(
        'User',
        backref=db.backref('pads', lazy='dynamic', cascade='all')
    )

    def __repr__(self):
        return '<Pad %r>' % self.name


__all__ = [ Pad ]