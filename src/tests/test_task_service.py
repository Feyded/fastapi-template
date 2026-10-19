from my_fastapi_app_v2.models.task import Task
from my_fastapi_app_v2.schemas.task import TaskCreate
from my_fastapi_app_v2.services.task_service import create_task, get_task


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


def test_create_task(db):
    new_task = TaskCreate(
        title="Created task",
        description="Testing create",
    )
    result = create_task(db, new_task)

    assert result.title == "Created task"
    assert result.id is not None

    task = get_task(db, result.id)

    assert task is not None

    assert task.title == new_task.title
    assert task.description == new_task.description
