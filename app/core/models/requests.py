import enum

from sqlalchemy import DateTime, String, Enum, Text
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from .base import Base
from .mixins.int_pk_mixin import IntPkMixin


class RequestStatus(enum.Enum):
    pending: str = "pending"
    canceled: str = "canceled"
    confirmed: str = "confirmed"


# TODO Add timestamp mixin
class Requests(Base, IntPkMixin):
    __tablename__: str = "requests"

    # TODO: make as a FK
    passenger_id: Mapped[int | None]
    operator_id: Mapped[int | None]

    # Marsroute points
    start_point: Mapped[str] = mapped_column(String(64))
    end_point: Mapped[str] = mapped_column(String(64))

    # TODO: make Mapped
    desired_trip_date = mapped_column(DateTime)

    notes: Mapped[str | None] = mapped_column(Text)
    status: Mapped[RequestStatus] = mapped_column(Enum(RequestStatus))

    # TODO Add relationships
