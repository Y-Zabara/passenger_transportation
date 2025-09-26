from fastapi import APIRouter

from core.schemas.requests import RequestPublic


router = APIRouter(
    prefix="/requests",
    tags=["requests"],
    )


@router.get("")
async def get_users():
    return {"text" : "Many users"}


@router.get("/{id}")
async def get_user_by_id(
    id: int,
    ):
    return {"text" : "Only one"}


@router.post("")
async def create_user():
    return {"text" : "Created User"}


@router.delete("/{id}")
async def delete_request(
    id: int,
    ):
    return {"text" : "Delete one"}

