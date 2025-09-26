from sqlalchemy.orm import Mapped

from .base import Base


class Tests(Base):
    __tablename__: str = "Tests"
    username: Mapped[str]
