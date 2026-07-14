from flask import Blueprint, jsonify

notes_bp = Blueprint('notes', __name__, url_prefix='/notes')

@notes_bp.route('/')
def notes_index():
    return jsonify({'notes': []})
