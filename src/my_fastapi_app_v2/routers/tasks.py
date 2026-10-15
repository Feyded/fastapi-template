from fastapi import APIRouter, HTTPException, Response, status

from my_fastapi_app_v2.schemas.task import TaskCreate, TaskUpdate

router = APIRouter()

tasks = {
    1: {
        "id": 1,
        "title": "Learn FastAPI",
        "description": "Study API development",
        "status": "pending",
    },
    2: {
        "id": 2,
        "title": "Learn Pydantic",
        "description": "Study request validation",
        "status": "pending",
    },
}


@router.get("/{task_id}")
def get_task(task_id: int):
    task = tasks.get(task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"data": task, "message": "Task retrieved successfully"}


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    del tasks[task_id]

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/")
def list_tasks():
    return {"data": tasks, "message": "Tasks retrieved successfully"}


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):

    task_id = max(tasks.keys(), default=0) + 1

    new_task = {"id": task_id, **task.model_dump(), "status": "pending"}

    tasks[task_id] = new_task

    return {
        "message": "Task created successfully",
        "task": new_task,
    }


@router.patch("/{task_id}")
def update_task(task_id: int, task: TaskUpdate):

    existing_task = tasks.get(task_id)

    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    updates = task.model_dump(exclude_unset=True)

    existing_task.update(updates)

    return {
        "message": "Task update received",
        "updates": existing_task,
    }
