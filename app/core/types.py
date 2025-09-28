from enum import Enum


class RequestStatus(str, Enum):
    pending: str = "pending"
    canceled: str = "canceled"
    confirmed: str = "confirmed"


class UserRole(str, Enum):
    user: str = "user"
    operator: str = "operator"
    admin: str = "admin"
