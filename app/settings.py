from pydantic_settings import BaseSettings
from pydantic import BaseModel


class Config(BaseSettings):
    pass


class RunCongfig(BaseModel):
    pass


class DbConfig(BaseModel):
    pass
