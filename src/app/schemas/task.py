from datetime import date

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.user import UserResponse


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(max_length=500)
    priority: int | None = None
    due_date: date | None = None


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    status: str | None = None
    priority: int | None = None
    due_date: date | None = None


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None
    status: str
    priority: int
    due_date: date | None
    user: UserResponse


class TaskSingleResponse(BaseModel):
    message: str
    data: TaskResponse


class TaskListResponse(BaseModel):
    message: str
    data: list[TaskResponse]
