from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from .base import Base
from .mixins.int_pk_mixin import IntPkMixin
from core.types import UserRole


# TODO: Add timestamp mixin
class Users(Base, IntPkMixin):
    __tablename__: str = "users"

    # personal information
    name: Mapped[str] = mapped_column(String(64))
    surname: Mapped[str | None] = mapped_column(String(64))
    # TODO validate phone
    phone: Mapped[str]

    # TODO: check
    hashed_password: Mapped[str]

    role: Mapped[UserRole] = mapped_column(default=UserRole.user)
    active: Mapped[bool] = mapped_column(default=True)

    # TODO: Add relationships

