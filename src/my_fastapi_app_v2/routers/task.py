from fastapi import APIRouter, Depends, Response, status

from my_fastapi_app_v2.dependencies import CurrentUser, DbSession, require_role
from my_fastapi_app_v2.schemas.task import (
    TaskCreate,
    TaskListResponse,
    TaskSingleResponse,
    TaskUpdate,
)
from my_fastapi_app_v2.services import task as task_service

router = APIRouter(
    prefix="/tasks", tags=["Tasks"], dependencies=[Depends(require_role(["user"]))]
)


@router.get("/", response_model=TaskListResponse)
def list_tasks(db: DbSession):
    tasks = task_service.list_tasks(db)

    return {
        "message": "Tasks retrieved successfully",
        "data": tasks,
    }


@router.get("/{task_id}", response_model=TaskSingleResponse)
def get_task(
    task_id: int,
    db: DbSession,
):
    task = task_service.get_task(db, task_id)

    return {
        "message": "Task retrieved successfully",
        "data": task,
    }


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: DbSession):
    task_service.delete_task(db, task_id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post(
    "/", response_model=TaskSingleResponse, status_code=status.HTTP_201_CREATED
)
def create_task_endpoint(payload: TaskCreate, db: DbSession, current_user: CurrentUser):
    task = task_service.create_task(db, payload, current_user)

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
    payload: TaskUpdate,
    db: DbSession,
):

    updated_task = task_service.update_task(
        db,
        task_id,
        payload,
    )

    return {
        "message": "Task updated successfully",
        "data": updated_task,
    }
