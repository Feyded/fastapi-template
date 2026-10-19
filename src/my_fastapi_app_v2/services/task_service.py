from sqlalchemy import select
from sqlalchemy.orm import Session

from my_fastapi_app_v2.models.task import Task
from my_fastapi_app_v2.schemas.task import TaskCreate


def list_tasks(db: Session) -> list[Task]:
    return db.scalars(select(Task)).all()


def get_task(db: Session, task_id: int) -> Task | None:
    return db.get(Task, task_id)


def create_task(
    db: Session,
    task_data: TaskCreate,
) -> Task:

    new_task = Task(
        title=task_data.title,
        description=task_data.description,
        status="pending",
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


def update_task(
    db: Session,
    task_id: int,
    updates: dict,
) -> Task | None:
    task = db.get(Task, task_id)

    if task is None:
        return None

    for field, value in updates.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)

    return task
