from sqlalchemy import select
from sqlalchemy.orm import Session

from my_fastapi_app_v2.exceptions import ConflictError, NotFoundError
from my_fastapi_app_v2.models.task import Task
from my_fastapi_app_v2.schemas.task import TaskCreate, TaskUpdate


def list_tasks(db: Session) -> list[Task]:
    return db.scalars(select(Task)).all()


def get_task(db: Session, task_id: int) -> Task | None:
    task = db.get(Task, task_id)

    if task is None:
        raise NotFoundError("Task not found.")

    return task


def create_task(
    db: Session,
    task_data: TaskCreate,
) -> Task:

    existing_task_id = db.scalar(select(Task.id).where(Task.title == task_data.title))

    if existing_task_id is not None:
        raise ConflictError("A task with this title already exists.")

    new_task = Task(**task_data.model_dump(exclude_unset=True), status="pending")

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def update_task(
    db: Session,
    task_id: int,
    task_data: TaskUpdate,
) -> Task | None:
    task = db.get(Task, task_id)

    if task is None:
        raise NotFoundError("Task not found")

    update_data = task_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)

    return task


def delete_task(db: Session, task_id: int) -> Task | None:
    task = db.get(Task, task_id)

    if task is None:
        raise NotFoundError("Task not found")

    db.delete(task)

    db.commit()

    return task
