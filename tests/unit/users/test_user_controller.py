# tests/unit/users/test_user_controller.py
from users import user_controller
from users.user_schemas import UserInput


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


def test_create_user_success():
    """Garante que a criação de usuário via controller persiste o novo registro."""
    user_input = UserInput(username="novo_usuario", email="novo@example.com")
    user = user_controller.create_user(user_input)
    assert user.id is not None
    assert user.username == "novo_usuario"
    assert user.email == "novo@example.com"

    fetched = user_controller.get_user_by_id(user.id)
    assert fetched is not None
    assert fetched.username == "novo_usuario"
