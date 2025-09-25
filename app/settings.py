from pydantic_settings import BaseSettings
from pydantic import BaseModel


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class DbConfig(BaseModel):
    url: str


class Config(BaseSettings):
    run: RunConfig = RunConfig()
    db: DbConfig
