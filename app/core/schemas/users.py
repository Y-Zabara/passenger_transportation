from  pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    surname: str
    # TODO validate phone
    phone: str
    # TODO validate role
    role: str


class UserCreate(UserBase):
    # TODO: validate password
    password: str


class UserUpdate(UserCreate):
    pass


class UserPublic(UserBase):
    id: int
    hashed_password: int


class UserLogin(BaseModel):
    # TODO: validate
    phone: str
    password: str
