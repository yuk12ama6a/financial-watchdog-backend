from fastapi.testclient import TestClient
from pytest_mock import MockFixture

from src.config import Settings
from src.main import app

client = TestClient(app=app)


def test_get_version(mocker: MockFixture) -> None:
    mocker.patch(
        "src.routers.version.Settings",
        return_value=Settings(VERSION="1.0.0-test"),
    )

    response = client.get(url="/api/version")

    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0-test"}
