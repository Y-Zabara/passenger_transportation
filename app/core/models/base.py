from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedColumn,
)


class Base(DeclarativeBase):
    __abstract__: bool = True

    id: Mapped[int] = MappedColumn(primary_key=True)
