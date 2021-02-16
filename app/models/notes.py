from ..models import db
import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey

class Note(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    text = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now
    )

    user_id = Column(Integer, ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('notes', lazy='dynamic'))

    pad_id = db.Column(Integer, ForeignKey('pad.id'))
    pad = db.relationship(
        'Pad',
        backref=db.backref('notes', lazy='dynamic', cascade='all')
    )

    def __repr__(self):
        return '<Note %r>' % self.name

__all__ = [ Note ]