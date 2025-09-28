from typing import Annotated
from jwt.exceptions import InvalidTokenError
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from fastapi.security import (
    OAuth2PasswordBearer,
)

from core.models.users import Users
from core.auth import utils as auth_utils
from api.dependencies import user_by_id, user_by_phone, SessionDependence

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/jwt/login",
)


async def authenticate_user(
    username: str,
    password: str,
    session,
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid username or password",
    )
    if not (user := await user_by_phone(session=session, phone=username)):
        raise unauthed_exc

    if not auth_utils.validate_password(
        password=password,
        hashed_password=user.hashed_password
    ):
        raise unauthed_exc

    if not user.active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="user inactive",
        )

    return user


def get_current_token_payload(
    token: str = Depends(oauth2_scheme),
):
    # token = credentials.credentials
    try:
        payload = auth_utils.decode_jwt(
            token=token,
        )
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"invalid token error: {e}",
            # detail=f"invalid token error",
        )
    return payload


def get_current_auth_user(
    session: SessionDependence,
    payload: dict = Depends(get_current_token_payload),
):
    user_id: str | None = payload.get("sub")
    if (user := user_by_id(id=user_id, session=session)):
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token invalid (user not found)",
    )


def get_current_active_auth_user(
    user = Depends(get_current_auth_user),
):
    if user.active:
        return user
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="user inactive",
    )


CurrentActiveUserDependence = Annotated[Users, get_current_active_auth_user]
AuthUserDependence = Annotated[Users, authenticate_user]
