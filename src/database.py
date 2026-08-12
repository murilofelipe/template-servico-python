"""Database module exposing Flask-SQLAlchemy and Flask-Migrate instances."""

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
