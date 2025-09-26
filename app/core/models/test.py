from sqlalchemy.orm import Mapped

from .base import Base
from .mixins.int_pk_mixin import IntPkMixin


class Tests(IntPkMixin, Base):
    __tablename__: str = "Tests"
    username: Mapped[str]
