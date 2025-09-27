from typing import Annotated
from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.models.users import Users
from core.models.requests import Requests
from core.schemas.users import UserPublic
from core.schemas.requests import RequestPublic

import crud.users as crud_users
import crud.requests as crud_requests


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


async def request_by_id(
    id: Annotated[int, Path],
    session: SessionDependence,
    ) -> Requests:
    request: Requests = await crud_requests.get_request_by_id(id=id, session=session)
    if request is not None:
        return request

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {id} not found",
    )
RequestDependence = Annotated[RequestPublic, Depends(request_by_id)]


