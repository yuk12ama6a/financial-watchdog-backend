from fastapi.testclient import TestClient
from pytest_mock import MockFixture

from src.config.settings import Settings
from src.main import app

client = TestClient(app=app)


def test_get_version(mocker: MockFixture) -> None:
    mocker.patch(
        "src.routers.version.Settings",
        return_value=Settings(MAJOR_VERSION=1, MINOR_VERSION=0, PATCH_VERSION=0),
    )

    response = client.get(url="/api/version")

    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}
