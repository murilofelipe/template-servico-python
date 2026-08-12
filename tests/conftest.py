# tests/conftest.py
import pytest
from flask import Flask
from flask.testing import FlaskClient

from database import db
from main import create_app
from users.user_models import UserModel


@pytest.fixture(scope="function", autouse=True)
def app_context():
    """Cria a aplicação Flask, configura banco em memória,
    semeia dados e limpa ao final.
    """
    flask_app = create_app()
    flask_app.config["TESTING"] = True
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with flask_app.app_context():
        db.create_all()

        # Seed de dados iniciais para retrocompatibilidade dos testes existentes
        user1 = UserModel(id=1, username="murilo", email="murilo@example.com")
        user2 = UserModel(id=2, username="gemini", email="gemini@example.com")
        db.session.add_all([user1, user2])
        db.session.commit()

        yield flask_app

        db.session.remove()
        db.drop_all()


@pytest.fixture(scope="function")
def test_client(app_context: Flask) -> FlaskClient:
    """Cria um cliente de teste para a aplicação Flask."""
    return app_context.test_client()
