from fastapi import APIRouter
from src.routers import user

router = APIRouter(
    prefix="/api"
)

router.include_router(user)