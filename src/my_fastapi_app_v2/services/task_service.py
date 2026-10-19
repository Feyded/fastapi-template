from sqlalchemy.orm import Session

from my_fastapi_app_v2.models.task import Task


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
