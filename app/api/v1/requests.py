from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.models.requests import Requests
from core.schemas.requests import RequestCreate, RequestPublic
import crud.requests as crud_requests


router = APIRouter(
    prefix="/requests",
    tags=["requests"],
)


SessionDependence = Annotated[AsyncSession, Depends(db_helper.session_getter)]

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


@router.get("", response_model=list[RequestPublic])
async def get_users(
    session: SessionDependence,
    ):
    return await crud_requests.get_requests(session=session)


@router.get("/{id}", response_model=RequestPublic)
async def get_user_by_id(
    request: RequestDependence,
    ):
    return request


@router.post("",
    response_model=RequestPublic,
    status_code=status.HTTP_201_CREATED,
    )
async def create_request(
    request_in: RequestCreate,
    session: SessionDependence,
    ):
    return await crud_requests.create_request(
        session=session,
        request_in=request_in,
    )


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_request(
    session: SessionDependence,
    request: RequestDependence,
    ) -> None:

    await crud_requests.delete_request(session=session, request=request)

