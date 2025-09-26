from sqlalchemy import MetaData
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedColumn,
)

from settings import config


class Base(DeclarativeBase):
    __abstract__: bool = True

    metadata = MetaData(
        naming_convention=config.db.naming_convention,
    )

    id: Mapped[int] = MappedColumn(primary_key=True)
