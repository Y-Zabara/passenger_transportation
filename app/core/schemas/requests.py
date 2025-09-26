from datetime import datetime
from pydantic import BaseModel, ConfigDict


class RequestBase(BaseModel):
    passenger_id: int
    operator_id: int | None
    start_point: str
    end_point: str
    desired_trip_date: datetime
    notes: str | None


class RequestCreate(RequestBase):
    pass


class RequestPublic(RequestBase):
    id: int
    status: str

    model_config = ConfigDict(
        from_attributes=True,
    )
