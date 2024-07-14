from fastapi import APIRouter

from src.config import Settings
from src.responses.version import VersionResponse

router = APIRouter()


@router.get(path="/version")
def get_version() -> VersionResponse:
    """
    サーバアプリのバージョンを返す
    """

    settings = Settings()

    return VersionResponse(version=settings.VERSION)
