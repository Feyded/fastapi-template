from my_fastapi_app_v2.models.task import Task
from my_fastapi_app_v2.services.task_service import get_task


def test_get_task_returns_task_when_found(db):
    task = Task(
        title="Test task",
        description="Learning pytest",
        status="pending",
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    result = get_task(db, task.id)

    assert result is not None
    assert result.title == "Test task"


def test_get_task_returns_none_when_not_found(db):
    result = get_task(db, 999999999)
    assert result is None
