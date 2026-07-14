import os
from flask import Flask, render_template, redirect, url_for, session, flash
from models import User, Note
from config import config
from extensions import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    os.makedirs(app.instance_path, exist_ok=True)

    try:
        from routes.auth import auth_bp
        from routes.notes import notes_bp
        from routes.api import api_bp

        app.register_blueprint(auth_bp)
        app.register_blueprint(notes_bp)
        app.register_blueprint(api_bp)

    except ImportError:
        pass

    @app.route("/")
    def home():
        return render_template('index.html')

    @app.route('/dashboard')
    def dashboard():
        if 'user_id' not in session:
            flash('Please log in to view your notes.', 'warning')
            return redirect(url_for('auth.login'))
        return redirect(url_for('notes.notes_index'))

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)