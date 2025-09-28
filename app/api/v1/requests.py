from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path, status

from core.schemas.requests import RequestCreate, RequestPublic
from api.dependencies.base import SessionDependence, RequestDependence
from api.dependencies.auth import AuthUserDependence, get_current_token_payload
import crud.requests as crud_requests



router = APIRouter(
    prefix="/requests",
    tags=["requests"],
)


@router.get("", response_model=list[RequestPublic])
async def get_requests(
    session: SessionDependence,
    payload: Annotated[dict, Depends(get_current_token_payload)],
    ):
    return await crud_requests.get_requests(session=session)


@router.get("/{id}", response_model=RequestPublic)
async def get_request_by_id(
    request: RequestDependence,
    payload: Annotated[dict, Depends(get_current_token_payload)],
    ):
    return request


@router.post("",
    response_model=RequestPublic,
    status_code=status.HTTP_201_CREATED,
    )
async def create_request(
    request_in: RequestCreate,
    session: SessionDependence,
    payload: Annotated[dict, Depends(get_current_token_payload)],
    ):
    return await crud_requests.create_request(
        session=session,
        request_in=request_in,
    )


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_request(
    session: SessionDependence,
    request: RequestDependence,
    payload: Annotated[dict, Depends(get_current_token_payload)],
    ) -> None:

    await crud_requests.delete_request(session=session, request=request)

