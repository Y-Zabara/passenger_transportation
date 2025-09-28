from fastapi import APIRouter, Depends, HTTPException, Path, status

from core.schemas.requests import RequestCreate, RequestPublic
from api.dependencies.base import SessionDependence, RequestDependence
import crud.requests as crud_requests



router = APIRouter(
    prefix="/requests",
    tags=["requests"],
)


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

