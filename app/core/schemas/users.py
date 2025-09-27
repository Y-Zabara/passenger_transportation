from  pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    surname: str
    # TODO validate phone
    phone: str


class UserCreate(UserBase):
    hashed_password: str


class UserRegistr(UserBase):
    password: str


class UserUpdate(UserCreate):
    pass


class UserPublic(UserBase):
    id: int
    hashed_password: str


class UserLogin(BaseModel):
    # TODO: validate
    phone: str
    password: str
