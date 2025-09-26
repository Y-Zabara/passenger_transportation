from sqlalchemy import MetaData
from sqlalchemy.orm import (
    DeclarativeBase,
)

from settings import config


class Base(DeclarativeBase):
    __abstract__: bool = True

    metadata = MetaData(
        naming_convention=config.db.naming_convention,
    )
