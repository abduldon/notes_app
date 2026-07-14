from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from extensions import db
from models import Note

notes_bp = Blueprint('notes', __name__, url_prefix='/notes')


def login_required():
    if 'user_id' not in session:
        flash('Please log in to access notes.', 'warning')
        return redirect(url_for('auth.login'))
    return None


@notes_bp.route('/')
def notes_index():
    redirect_response = login_required()
    if redirect_response:
        return redirect_response

    notes = Note.query.filter_by(user_id=session['user_id']).order_by(Note.id.desc()).all()
    return render_template('notes.html', notes=notes)


@notes_bp.route('/create', methods=['POST'])
def create_note():
    redirect_response = login_required()
    if redirect_response:
        return redirect_response

    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()

    if not title or not description:
        flash('Title and note content are required.', 'danger')
        return redirect(url_for('notes.notes_index'))

    note = Note(title=title, description=description, user_id=session['user_id'])
    db.session.add(note)
    db.session.commit()

    flash('Note added successfully.', 'success')
    return redirect(url_for('notes.notes_index'))


@notes_bp.route('/<int:note_id>/edit', methods=['GET', 'POST'])
def edit_note(note_id):
    redirect_response = login_required()
    if redirect_response:
        return redirect_response

    note = Note.query.filter_by(id=note_id, user_id=session['user_id']).first_or_404()

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()

        if not title or not description:
            flash('Both title and content are required.', 'danger')
            return render_template('edit_note.html', note=note)

        note.title = title
        note.description = description
        db.session.commit()

        flash('Note updated successfully.', 'success')
        return redirect(url_for('notes.notes_index'))

    return render_template('edit_note.html', note=note)


@notes_bp.route('/<int:note_id>/delete', methods=['POST'])
def delete_note(note_id):
    redirect_response = login_required()
    if redirect_response:
        return redirect_response

    note = Note.query.filter_by(id=note_id, user_id=session['user_id']).first_or_404()
    db.session.delete(note)
    db.session.commit()

    flash('Note deleted.', 'success')
    return redirect(url_for('notes.notes_index'))
