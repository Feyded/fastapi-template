# from my_fastapi_app_v2.models.task import Task
# from my_fastapi_app_v2.schemas.task import TaskCreate, TaskUpdate
# from my_fastapi_app_v2.services.task_service import (
#     create_task,
#     delete_task,
#     get_task,
#     update_task,
# )


# def test_get_task_returns_task_when_found(db):
#     task = Task(
#         title="Test task",
#         description="Learning pytest",
#         status="pending",
#     )

#     db.add(task)
#     db.commit()
#     db.refresh(task)

#     result = get_task(db, task.id)

#     assert result is not None
#     assert result.title == "Test task"


# def test_get_task_returns_none_when_not_found(db):
#     result = get_task(db, 999999999)
#     assert result is None


# def test_create_task(db):
#     new_task = TaskCreate(
#         title="Created task",
#         description="Testing create",
#     )
#     result = create_task(db, new_task)

#     assert result.title == "Created task"
#     assert result.id is not None

#     task = get_task(db, result.id)

#     assert task is not None

#     assert task.title == new_task.title
#     assert task.description == new_task.description


# def test_update_task(db):
#     task_data = TaskCreate(
#         title="Created task",
#         description="Testing create",
#     )

#     created_task = create_task(db, task_data)

#     task_update = TaskUpdate(title="Updated title")

#     updated_task = update_task(
#         db,
#         created_task.id,
#         task_update.model_dump(exclude_unset=True),
#     )

#     assert updated_task is not None
#     assert updated_task.title == "Updated title"
#     assert updated_task.description == "Testing create"


# def test_update_task_returns_none_when_not_found(db):
#     updated_task = update_task(
#         db,
#         999999,
#         {"title": "Updated title"},
#     )

#     assert updated_task is None


# def test_delete_task(db):
#     task_data = TaskCreate(title="test title", description="test title")

#     created_task = create_task(
#         db,
#         task_data,
#     )

#     deleted_task = delete_task(
#         db,
#         created_task.id,
#     )

#     assert deleted_task is not None
#     assert deleted_task.id == created_task.id

#     task = get_task(
#         db,
#         created_task.id,
#     )

#     assert task is None


# def test_delete_task_returns_none_when_not_found(db):

#     deleted_task = delete_task(
#         db,
#         999999,
#     )

#     assert deleted_task is None
