# src/main.py
from flask import Flask

from core.config import settings
from database import db, migrate
from healthcheck.health_routes import health_bp
from users.user_models import UserModel  # noqa: F401
from users.user_routes import user_bp


def create_app() -> Flask:
    """Cria e configura a instância da aplicação Flask."""
    app = Flask(__name__)

    # Carrega configurações centralizadas no Flask app.config
    app.config["ENVIRONMENT"] = settings.ENVIRONMENT
    app.config["DEBUG"] = settings.DEBUG
    app.config["PORT"] = settings.PORT
    app.config["DATABASE_URL"] = settings.DATABASE_URL
    app.config["SQLALCHEMY_DATABASE_URI"] = settings.DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["APP_NAME"] = settings.APP_NAME

    # Inicializa extensões de banco de dados e migrações
    db.init_app(app)
    migrate.init_app(app, db)

    # Registra os blueprints na aplicação
    app.register_blueprint(health_bp)
    app.register_blueprint(user_bp)

    @app.route("/")
    def index():
        return (
            "<h1>Bem-vindo à API do nosso serviço!</h1><p>Acesse /users ou /health.</p>"
        )

    return app
