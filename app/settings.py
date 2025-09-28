from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn

from pathlib import Path


BASE_DIR = Path(__file__).parent

class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class DbConfig(BaseModel):
    url: PostgresDsn = ""
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class AuthConfig(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15


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
    auth_jwt: AuthConfig = AuthConfig()


config = Config()
