from flask import current_app
from flask_login import (login_required, current_user)
from flask import render_template, request

from ..models import Note

@current_app.route('/')
@login_required
def home():
    notes = (Note.query
                 .filter_by(user=current_user)
                 .order_by(_get_order_by(request.args.get('order')))
                 .all())
    return render_template('notes/list.html', notes=notes)

def _get_order_by(param='-updated_at'):
    ''' get model order param by string description '''
    return {
        'name': Note.name.asc(),
        '-name': Note.name.desc(),
        'updated_at': Note.updated_at.asc(),
        '-updated_at': Note.updated_at.desc(),
    }.get(param, Note.updated_at.desc())
