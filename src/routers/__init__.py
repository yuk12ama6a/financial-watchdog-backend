from fastapi import APIRouter

from src.routers.health import router as health_router
from src.routers.version import router as version_router

router = APIRouter(prefix="/api")
router.include_router(router=health_router)
router.include_router(router=version_router)
