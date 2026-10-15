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


@router.post("/", status_code=status.HTTP_201_CREATED)
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
        "task": new_task,
    }


@router.patch("/{task_id}")
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
):
    existing_task = db.get(Task, task_id)

    if existing_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    updates = task.model_dump(exclude_unset=True)

    for field, value in updates.items():
        setattr(existing_task, field, value)

    db.commit()
    db.refresh(existing_task)

    return {
        "message": "Task updated successfully",
        "data": {
            "id": existing_task.id,
            "title": existing_task.title,
            "description": existing_task.description,
            "status": existing_task.status,
        },
    }
