from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from my_fastapi_app_v2.database import Base
from my_fastapi_app_v2.models.task import Task


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    tasks: Mapped[list[Task]] = relationship(back_populates="user")
