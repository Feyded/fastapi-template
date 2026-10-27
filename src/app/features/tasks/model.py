from datetime import date

from sqlalchemy import Date, ForeignKey, String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.shared.mixins import TimestampMixin


class Task(TimestampMixin, Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    description: Mapped[str] = mapped_column(String(500), nullable=False)

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="pending",
        server_default=text("'pending'"),
    )

    priority: Mapped[int] = mapped_column(
        default=1,
        server_default=text("1"),
        nullable=False,
    )

    due_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    user: Mapped["User"] = relationship(back_populates="tasks")
