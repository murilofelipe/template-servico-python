# src/users/user_controller.py
from typing import List
from .user_schemas import User

# Dados de exemplo. Em um projeto real, isso viria de um banco de dados.
fake_db: List[User] = [
    User(id=1, username="murilo", email="murilo@example.com"),
    User(id=2, username="gemini", email="gemini@example.com"),
]


def get_all_users() -> List[User]:
    """Retorna todos os usuários."""
    return fake_db


def get_user_by_id(user_id: int) -> User | None:
    """Busca um usuário específico pelo seu ID.

    Esta função itera sobre a lista de usuários em memória para encontrar
    uma correspondência com o ID fornecido.

    Args:
        user_id: O ID numérico do usuário a ser encontrado.

    Returns:
        Um objeto User se o usuário for encontrado, caso contrário, None.
    """
    for user in fake_db:
        if user.id == user_id:
            return user
    return None
