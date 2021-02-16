from flask import current_app
from flask import render_template, flash, request, redirect, url_for, abort

from flask_login import (login_required, current_user)
from ..models import Pad, Note, db
from ..forms import (PadForm, DeleteForm)

@current_app.route('/pads/create/', methods=['GET', 'POST'])
@login_required
def create_pad():
    pad_form = PadForm()
    if pad_form.validate_on_submit():
        pad = Pad(
            name=pad_form.name.data,
            user=current_user
        )
        db.session.add(pad)
        db.session.commit()
        flash('Pad is successfully created', 'success')
        return redirect(url_for('home'))
    return render_template('pads/create.html', form=pad_form)


@current_app.route('/pads/<int:pad_id>/edit/', methods=['GET', 'POST'])
@login_required
def edit_pad(pad_id):
    pad = _get_user_object_or_404(Pad, pad_id, current_user)
    pad_form = PadForm(obj=pad)
    if pad_form.validate_on_submit():
        pad.name = pad_form.name.data
        db.session.commit()
        flash('Pad is successfully updated', 'success')
        return redirect(url_for('pad_notes', pad_id=pad.id))
    return render_template('pads/edit.html', form=pad_form, pad=pad)


@current_app.route('/pads/<int:pad_id>/')
@login_required
def pad_notes(pad_id):
    pad = _get_user_object_or_404(Pad, pad_id, current_user)
    notes = (Note.query
                 .filter_by(user=current_user, pad=pad)
                 .order_by(_get_order_by(request.args.get('order')))
                 .all())
    return render_template('pads/note_list.html', pad=pad, notes=notes)


@current_app.route('/pads/<int:pad_id>/delete/', methods=['GET', 'POST'])
@login_required
def delete_pad(pad_id):
    pad = _get_user_object_or_404(Pad, pad_id, current_user)
    delete_form = DeleteForm()
    if request.method == 'POST':
        db.session.delete(pad)
        db.session.commit()
        flash('Note is successfully deleted', 'success')
        return redirect(url_for('home'))
    return render_template('pads/delete.html', pad=pad, form=delete_form)

# context processors and filters
@current_app.context_processor
def inject_user_pads():
    ''' inject list of user pads in template context '''
    if not current_user.is_anonymous:
        return dict(pads=current_user.pads.all())
    return dict(pads=[])

def _get_user_object_or_404(model, object_id, user, code=404):
    ''' get an object by id and owner user or raise an abort '''
    result = model.query.filter_by(id=object_id, user=user).first()
    return result or abort(code)

def _get_order_by(param='-updated_at'):
    ''' get model order param by string description '''
    return {
        'name': Note.name.asc(),
        '-name': Note.name.desc(),
        'updated_at': Note.updated_at.asc(),
        '-updated_at': Note.updated_at.desc(),
    }.get(param, Note.updated_at.desc())
