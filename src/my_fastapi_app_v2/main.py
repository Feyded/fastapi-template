from fastapi import FastAPI

from my_fastapi_app_v2.exception_handlers import app_error_handler
from my_fastapi_app_v2.exceptions import AppError
from my_fastapi_app_v2.routers.tasks import router as tasks_router

app = FastAPI(title="Task Management API")

app.include_router(tasks_router, prefix="/tasks", tags=["Tasks"])

app.add_exception_handler(AppError, app_error_handler)


@app.get("/")
def root():
    return {"message": "Task Management API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
