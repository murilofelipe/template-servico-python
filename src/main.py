# src/main.py
from flask import Flask

# Importa os blueprints das features
from .users.user_routes import user_bp
from .healthcheck.health_routes import health_bp


def create_app():
    """Cria e configura a instância da aplicação Flask."""
    app = Flask(__name__)

    # Registra os blueprints na aplicação
    app.register_blueprint(health_bp)
    app.register_blueprint(user_bp)

    @app.route("/")
    def index():
        return (
            "<h1>Bem-vindo à API do nosso serviço!</h1><p>Acesse /users ou /health.</p>"
        )

    return app
