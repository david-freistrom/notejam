from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import Required

from ..models import Pad

class NoteForm(FlaskForm):
    name = StringField('Name', validators=[Required()])
    text = TextAreaField('Note', validators=[Required()])
    pad = SelectField('Pad', choices=[], coerce=int)

    # @TODO use wtforms.ext.sqlalchemy.fields.QuerySelectField?
    def __init__(self, user=None, **kwargs):
        super(NoteForm, self).__init__(**kwargs)
        self.pad.choices = [(0, '---------')] + [
            (p.id, p.name) for p in Pad.query.filter_by(user=user)
        ]

__all__ = [ NoteForm ]
