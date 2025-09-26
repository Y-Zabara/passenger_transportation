from sqlalchemy.orm import Mapped, MappedColumn


class IntPkMixin:
    id: Mapped[int] = MappedColumn(primary_key=True)

