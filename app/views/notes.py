from flask import current_app
from flask_login import (login_required, current_user)
from flask import render_template, request, flash, redirect, url_for, abort
from ..models import Note, db
from ..forms import (NoteForm, DeleteForm)

@current_app.route('/notes/create/', methods=['GET', 'POST'])
@login_required
def create_note():
    note_form = NoteForm(user=current_user, pad=request.args.get('pad'))
    if note_form.validate_on_submit():
        note = Note(
            name=note_form.name.data,
            text=note_form.text.data,
            pad_id=note_form.pad.data,
            user=current_user
        )
        db.session.add(note)
        db.session.commit()
        flash('Note is successfully created', 'success')
        return redirect(_get_note_success_url(note))
    return render_template('notes/create.html', form=note_form)


@current_app.route('/notes/<int:note_id>/edit/', methods=['GET', 'POST'])
@login_required
def edit_note(note_id):
    note = _get_user_object_or_404(Note, note_id, current_user)
    note_form = NoteForm(user=current_user, obj=note)
    if note_form.validate_on_submit():
        note.name = note_form.name.data
        note.text = note_form.text.data
        note.pad_id = note_form.pad.data

        db.session.commit()
        flash('Note is successfully updated', 'success')
        return redirect(_get_note_success_url(note))
    if note.pad:
        note_form.pad.data = note.pad.id  # XXX ?
    return render_template('notes/edit.html', form=note_form)


@current_app.route('/notes/<int:note_id>/')
@login_required
def view_note(note_id):
    note = _get_user_object_or_404(Note, note_id, current_user)
    return render_template('notes/view.html', note=note)


@current_app.route('/notes/<int:note_id>/delete/', methods=['GET', 'POST'])
@login_required
def delete_note(note_id):
    note = _get_user_object_or_404(Note, note_id, current_user)
    delete_form = DeleteForm()
    if request.method == 'POST':
        db.session.delete(note)
        db.session.commit()
        flash('Note is successfully deleted', 'success')
        return redirect(url_for('home'))
    return render_template('notes/delete.html', note=note, form=delete_form)


# helper functions, @TODO move to helpers.py?
def _get_note_success_url(note):
    ''' get note success redirect url depends on note's pad '''
    if note.pad is None:
        return url_for('home')
    else:
        return url_for('pad_notes', pad_id=note.pad.id)


def _get_user_object_or_404(model, object_id, user, code=404):
    ''' get an object by id and owner user or raise an abort '''
    result = model.query.filter_by(id=object_id, user=user).first()
    return result or abort(code)
