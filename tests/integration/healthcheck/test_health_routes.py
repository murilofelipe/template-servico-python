# tests/integration/healthcheck/test_health_routes.py
def test_health_route(test_client):
    response = test_client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
