from fastapi import APIRouter

from src.responses.health import HealthCheckResponse

router = APIRouter()


@router.get(path="/health")
def health_check() -> HealthCheckResponse:
    """
    ヘルスチェックを行う
    """

    return HealthCheckResponse()
