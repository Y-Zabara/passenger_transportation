from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.models.users import Users
from core.schemas.users import UserCreate, UserPublic, UserRegistr
import crud.users as crud_users


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


SessionDependence = Annotated[AsyncSession, Depends(db_helper.session_getter)]

async def user_by_id(
    id: Annotated[int, Path],
    session: SessionDependence,
    ) -> Users:
    user: Users = await crud_users.get_user_by_id(id=id, session=session)
    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {id} not found",
    )
UserDependence = Annotated[UserPublic, Depends(user_by_id)]


@router.get("", response_model=list[UserPublic])
async def get_users(
    session: SessionDependence,
    ):
    return await crud_users.get_users(session=session)


@router.get("/{id}", response_model=UserPublic)
async def get_user_by_id(
    user: UserDependence,
    ):
    return user


@router.post("",
    response_model=UserPublic,
    status_code=status.HTTP_201_CREATED,
    )
async def create_user(
    user_in: UserRegistr,
    session: SessionDependence,
    ):
    user: UserCreate = UserCreate(**user_in.dict(exclude={"password"}), hashed_password="hashed_password")
    return await crud_users.create_user(
        session=session,
        user_in=user,
    )


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    session: SessionDependence,
    user: UserDependence,
    ) -> None:

    await crud_users.delete_user(session=session, user=user)


