from fastapi import APIRouter

from src.routers.health import router as health_router

router = APIRouter(prefix="/api")
router.include_router(router=health_router)
