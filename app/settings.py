from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class DbConfig(BaseModel):
    url: PostgresDsn = ""
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Config(BaseSettings):
    """Config settings class.

        Args:
            env_file (tuple[str]): List of environment files. 
                Variables from the latter override those from the former.
            case_sensitive (bool): Whether to treat environment variable names 
                as case sensitive. Useful because fields are usually snake_case 
                while environment variables are often uppercase.
            env_nested_delimiter (str): Delimiter to support nested structures 
                in environment variables.
            env_prefix (str): Prefix to distinguish application-specific 
                environment variables.
    """
    model_config = SettingsConfigDict(
        env_file=(".env_example",".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FASTAPI__",
    )

    run: RunConfig = RunConfig()
    db: DbConfig = DbConfig()


config = Config()
