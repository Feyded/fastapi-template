from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from my_fastapi_app_v2.dependencies import CurrentUser
from my_fastapi_app_v2.exceptions import ConflictError, NotFoundError
from my_fastapi_app_v2.models.task import Task
from my_fastapi_app_v2.schemas.task import TaskCreate, TaskUpdate


def list_tasks(db: Session, page: int, limit: int) -> list[Task]:
    offset = (page - 1) * limit
    statement = (
        select(Task).options(selectinload(Task.user)).offset(offset).limit(limit)
    )
    return db.scalars(statement).all()


def get_task(db: Session, task_id: int) -> Task | None:
    task = db.get(Task, task_id)

    if task is None:
        raise NotFoundError("Task not found.")

    return task


def create_task(db: Session, task_data: TaskCreate, current_user: CurrentUser) -> Task:

    existing_task_id = db.scalar(select(Task.id).where(Task.title == task_data.title))

    if existing_task_id is not None:
        raise ConflictError("A task with this title already exists.")

    new_task = Task(
        **task_data.model_dump(exclude_unset=True),
        status="pending",
        user_id=current_user.id,
    )

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
