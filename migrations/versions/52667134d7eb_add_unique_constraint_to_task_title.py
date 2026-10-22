"""add unique constraint to task title

Revision ID: 52667134d7eb
Revises: 8f576a5674df
Create Date: 2026-10-22 11:06:01.896357

"""

from collections.abc import Sequence

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "52667134d7eb"
down_revision: str | Sequence[str] | None = "8f576a5674df"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    with op.batch_alter_table("tasks") as batch_op:
        batch_op.create_unique_constraint(
            "uq_tasks_title",
            ["title"],
        )


def downgrade() -> None:
    with op.batch_alter_table("tasks") as batch_op:
        batch_op.drop_constraint(
            "uq_tasks_title",
            type_="unique",
        )
