from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app=app)


def test_health_check() -> None:
    response = client.get(url="/api/health")

    assert response.status_code == 200
