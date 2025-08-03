# tests/integration/users/test_user_routes.py
def test_get_users_endpoint(test_client):
    """Garante que o endpoint GET /users retorna status 200 e os dados corretos."""
    response = test_client.get("/users/")
    assert response.status_code == 200
    json_data = response.get_json()
    assert isinstance(json_data, list)
    assert json_data[0]["username"] == "murilo"
