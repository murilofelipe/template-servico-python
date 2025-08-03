# tests/unit/users/test_user_controller.py
from src.users import user_controller


def test_get_all_users_returns_list():
    """Garante que o controller de usuários retorna uma lista."""
    users = user_controller.get_all_users()
    assert isinstance(users, list)
    assert len(users) > 0
    assert users[0].username == "murilo"
