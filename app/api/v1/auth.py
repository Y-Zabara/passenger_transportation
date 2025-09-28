from typing import Annotated
from fastapi import (
    APIRouter,
    Depends,
)
from fastapi.security import (
    OAuth2PasswordRequestForm,
)
from pydantic import BaseModel

from core.auth import utils as auth_utils
from api.dependencies.base import SessionDependence
from api.dependencies.auth import (
    get_current_active_auth_user,
    get_current_token_payload,
    authenticate_user,
)


class TokenInfo(BaseModel):
    access_token: str
    token_type: str


router = APIRouter(prefix="/auth/jwt", tags=["JWT"])


@router.post("/login", response_model=TokenInfo)
async def auth_user_issue_jwt(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: SessionDependence,
):
    user = await authenticate_user(form_data.username, form_data.password, session=session)
    jwt_payload = {
        # subject
        "sub": str(user.id),
        "username": user.phone,
        # "logged_in_at"
    }
    token = auth_utils.encode_jwt(jwt_payload)
    return TokenInfo(
        access_token=token,
        token_type="Bearer",
    )


@router.get("/me")
def auth_user_check_self_info(
    #payload: dict = Depends(get_current_token_payload),
    user = Depends(get_current_active_auth_user),
):
    return {
        "username": user.name,
    }
