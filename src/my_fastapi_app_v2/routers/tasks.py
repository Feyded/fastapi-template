from fastapi import APIRouter, Response, status

from my_fastapi_app_v2.dependencies import DbSession
from my_fastapi_app_v2.schemas.task import (
    TaskCreate,
    TaskListResponse,
    TaskSingleResponse,
    TaskUpdate,
)
from my_fastapi_app_v2.services.task_service import (
    create_task as create_task_service,
)
from my_fastapi_app_v2.services.task_service import (
    delete_task as delete_task_service,
)
from my_fastapi_app_v2.services.task_service import (
    get_task as get_task_service,
)
from my_fastapi_app_v2.services.task_service import (
    list_tasks as list_task_service,
)
from my_fastapi_app_v2.services.task_service import (
    update_task as update_task_service,
)

router = APIRouter()


@router.get("/", response_model=TaskListResponse)
def list_tasks(db: DbSession):
    tasks = list_task_service(db)

    return {
        "message": "Tasks retrieved successfully",
        "data": tasks,
    }


@router.get("/{task_id}", response_model=TaskSingleResponse)
def get_task(
    task_id: int,
    db: DbSession,
):
    task = get_task_service(db, task_id)

    return {
        "message": "Task retrieved successfully",
        "data": task,
    }


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: DbSession):
    delete_task_service(db, task_id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/", status_code=201)
def create_task_endpoint(
    task_data: TaskCreate,
    db: DbSession,
):
    task = create_task_service(db, task_data)

    return {
        "message": "Task created successfully",
        "data": task,
    }


@router.patch(
    "/{task_id}",
    response_model=TaskSingleResponse,
)
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: DbSession,
):

    updated_task = update_task_service(
        db,
        task_id,
        task,
    )

    return {
        "message": "Task updated successfully",
        "data": updated_task,
    }
