import os
from os import path

BASE_DIR = path.abspath(path.dirname(__file__))
INSTANCE_DIR = path.join(BASE_DIR, "instance")

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev_secret_key")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        f"sqlite:///{path.join(INSTANCE_DIR, 'app.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = Config()
