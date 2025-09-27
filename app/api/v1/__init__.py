from fastapi import APIRouter

from .items import router as item_router
from .requests import router as requests_router
from .users import router as users_router

v1_router = APIRouter(
    prefix="/v1",
)
v1_router.include_router(item_router)
v1_router.include_router(requests_router)
v1_router.include_router(users_router)
