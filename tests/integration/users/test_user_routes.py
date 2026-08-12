# tests/integration/users/test_user_routes.py
def test_get_users_endpoint(test_client):
    """Garante que o endpoint GET /users retorna status 200 e os dados corretos."""
    response = test_client.get("/users/")
    assert response.status_code == 200
    json_data = response.get_json()
    assert isinstance(json_data, list)
    assert json_data[0]["username"] == "murilo"


def test_get_user_by_id_route_found(test_client):
    response = test_client.get("/users/1")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["id"] == 1


def test_get_user_by_id_route_not_found(test_client):
    response = test_client.get("/users/999")
    assert response.status_code == 404
