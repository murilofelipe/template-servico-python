# tests/integration/test_docs.py


def test_swagger_docs_route(test_client):
    """Asserts GET /docs/ returns HTTP 200 with Swagger UI HTML content."""
    response = test_client.get("/docs/")
    assert response.status_code == 200
    content = response.get_data(as_text=True)
    assert "swagger-ui" in content.lower() or "swagger" in content.lower()


def test_openapi_json_route(test_client):
    """Asserts GET /openapi.json returns HTTP 200 with valid OpenAPI 3.0 schema."""
    response = test_client.get("/openapi.json")
    assert response.status_code == 200
    data = response.get_json()
    assert data["openapi"] == "3.0.3"
    assert "/health" in data["paths"]
    assert "/users/" in data["paths"]
    assert "/users/{user_id}" in data["paths"]
    assert "User" in data["components"]["schemas"]
    assert "UserInput" in data["components"]["schemas"]
