from fastapi import APIRouter

from src.config.settings import Settings
from src.responses.version import VersionResponse

router = APIRouter()


@router.get(path="/version")
def get_version() -> VersionResponse:
    """
    サーバアプリのバージョンを返す
    """

    settings = Settings()

    return VersionResponse(
        version=f"{settings.MAJOR_VERSION}.{settings.MINOR_VERSION}.{settings.PATCH_VERSION}"
    )
