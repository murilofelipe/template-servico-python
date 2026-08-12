# src/users/user_controller.py
from typing import List, Optional

from sqlalchemy.exc import IntegrityError

from database import db
from users.user_models import UserModel
from users.user_schemas import User, UserInput


def get_all_users() -> List[User]:
    """Retorna todos os usuários cadastrados no banco de dados."""
    users = UserModel.query.all()
    return [User.model_validate(u) for u in users]


def get_user_by_id(user_id: int) -> Optional[User]:
    """Busca um usuário específico pelo seu ID no banco de dados.

    Args:
        user_id: O ID numérico do usuário a ser encontrado.

    Returns:
        Um objeto User se o usuário for encontrado, caso contrário, None.
    """
    user = db.session.get(UserModel, user_id)
    if user:
        return User.model_validate(user)
    return None


def create_user(user_input: UserInput) -> User:
    """Cria e persiste um novo usuário no banco de dados.

    Args:
        user_input: Dados para criação do usuário.

    Returns:
        Um objeto User representando o usuário criado.

    Raises:
        IntegrityError: Se o username ou email já existirem no banco de dados.
    """
    user_model = UserModel(
        username=user_input.username,
        email=user_input.email,
    )
    db.session.add(user_model)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return User.model_validate(user_model)
