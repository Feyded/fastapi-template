from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from my_fastapi_app_v2.database import get_db
from my_fastapi_app_v2.models.task import Task
from my_fastapi_app_v2.schemas.task import (
    TaskCreate,
    TaskListResponse,
    TaskSingleResponse,
    TaskUpdate,
)
from my_fastapi_app_v2.services.task_service import (
    update_task as update_task_service,
)

router = APIRouter()


@router.get("/{task_id}", response_model=TaskSingleResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
):
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return {
        "message": "Task retrieved successfully",
        "data": task,
    }


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    db.delete(task)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/", response_model=TaskListResponse)
def list_tasks(db: Session = Depends(get_db)):
    tasks = db.scalars(select(Task)).all()

    return {
        "message": "Tasks retrieved successfully",
        "data": tasks,
    }


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=TaskSingleResponse,
)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
):
    new_task = Task(
        title=task.title,
        description=task.description,
        status="pending",
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {
        "message": "Task created successfully",
        "data": new_task,
    }


@router.patch(
    "/{task_id}",
    response_model=TaskSingleResponse,
)
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
):
    updates = task.model_dump(exclude_unset=True)

    updated_task = update_task_service(
        db,
        task_id,
        updates,
    )

    if updated_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return {
        "message": "Task updated successfully",
        "data": updated_task,
    }
