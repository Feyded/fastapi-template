from pydantic import BaseModel, ConfigDict, Field


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(max_length=500)


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    status: str | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str

    model_config = ConfigDict(from_attributes=True)


class TaskSingleResponse(BaseModel):
    message: str
    data: TaskResponse


class TaskListResponse(BaseModel):
    message: str
    data: list[TaskResponse]
