# tests/integration/healthcheck/test_health_routes.py


def test_health_route_success(test_client):
    """Asserts GET /health returns HTTP 200 and database connected status."""
    response = test_client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok", "database": "connected"}


def test_health_route_db_failure(test_client, monkeypatch):
    """Asserts GET /health returns HTTP 503 when database execution fails."""

    def mock_execute(*args, **kwargs):
        raise Exception("Database connection error")

    monkeypatch.setattr("database.db.session.execute", mock_execute)
    response = test_client.get("/health")
    assert response.status_code == 503
    assert response.get_json() == {
        "status": "unhealthy",
        "database": "disconnected",
    }

