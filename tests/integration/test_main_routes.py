# tests/integration/test_main_routes.py
def test_index_route(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"Bem-vindo" in response.data
