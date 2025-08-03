# tests/conftest.py
import pytest
from src.main import create_app


@pytest.fixture(scope="module")
def test_client():
    """Cria um cliente de teste para a aplicação Flask."""
    flask_app = create_app()

    # Cria um cliente de teste usando o contexto do Flask
    with flask_app.test_client() as testing_client:
        # Estabelece um contexto de aplicação
        with flask_app.app_context():
            yield testing_client  # Retorna o cliente para ser usado nos testes
