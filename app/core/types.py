from enum import Enum


class RequestStatus(Enum):
    pending: str = "pending"
    canceled: str = "canceled"
    confirmed: str = "confirmed"


class UserRole(Enum):
    user: str = "user"
    operator: str = "operator"
    admin: str = "admin"
