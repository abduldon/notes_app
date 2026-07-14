import os
from flask import Flask, request
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
    def hello_world():
        return """
        <h1>Hello, World!</h1>
        <p>My Notes App</p>
        <p>Project setup done and database connected.</p>
        """

    @app.route("/register", methods=["GET", "POST"])
    def register():

        if request.method == "POST":

            username = request.form["username"]
            email = request.form["email"]
            password = request.form["password"]

            user = User(
                username=username,
                email=email,
                password=password
            )

            db.session.add(user)
            db.session.commit()

            return "User Registered Successfully!"

        return """
        <form method="POST">
            Username:
            <input name="username"><br><br>

            Email:
            <input name="email"><br><br>

            Password:
            <input type="password" name="password"><br><br>

            <button type="submit">
                Register
            </button>
        </form>
        """

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)