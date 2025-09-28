from fastapi import APIRouter, Depends, HTTPException, Path, status

from core.schemas.users import UserCreate, UserPublic, UserRegistr
from api.dependencies.base import SessionDependence, UserDependence
from core.auth.utils import hash_password
import crud.users as crud_users


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


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
    user: UserCreate = UserCreate(
        **user_in.dict(exclude={"password"}),
        hashed_password=hash_password(user_in.password))
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


