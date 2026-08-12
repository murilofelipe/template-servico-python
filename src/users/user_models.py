"""SQLAlchemy UserModel entity definition."""

from datetime import datetime

from database import db


class UserModel(db.Model):
    """Modelo ORM de usuário para persistência no banco de dados."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return f"<UserModel id={self.id} username='{self.username}'>"
