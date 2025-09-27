from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from core.types import RequestStatus

from .base import Base
from .mixins.int_pk_mixin import IntPkMixin


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
    desired_trip_date = mapped_column(DateTime(timezone=True))

    notes: Mapped[str | None] = mapped_column(Text)
    status: Mapped[RequestStatus] = mapped_column(default=RequestStatus.pending)

    # TODO Add relationships
