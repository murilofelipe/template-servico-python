# tests/unit/users/test_user_controller.py
from users import user_controller


def test_get_all_users_returns_list():
    """Garante que o controller de usuários retorna uma lista."""
    users = user_controller.get_all_users()
    assert isinstance(users, list)
    assert len(users) > 0
    assert users[0].username == "murilo"


def test_get_user_by_id_found():
    user = user_controller.get_user_by_id(1)
    assert user is not None
    assert user.id == 1
    assert user.username == "murilo"


def test_get_user_by_id_not_found():
    user = user_controller.get_user_by_id(999)
    assert user is None
