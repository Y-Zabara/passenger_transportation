from fastapi import APIRouter

from .items import router as item_router

v1_router = APIRouter(
    prefix="/v1",
)
v1_router.include_router(item_router)
