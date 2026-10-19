from my_fastapi_app_v2.database import SessionLocal
from my_fastapi_app_v2.models.task import Task
from my_fastapi_app_v2.services.task_service import get_task


def test_get_task_returns_task_when_found():
    db = SessionLocal()
    try:
        task = Task(title="Test task", description="Learning pytest", status="pending")
        db.add(task)
        db.commit()
        db.refresh(task)
        result = get_task(db, task.id)
        assert result is not None
        assert result.title == "Test task"
    finally:
        db.close()
