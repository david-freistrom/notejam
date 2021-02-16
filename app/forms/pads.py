from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Required

class PadForm(FlaskForm):
    name = StringField('Name', validators=[Required()])

__all__ = [ PadForm ]
