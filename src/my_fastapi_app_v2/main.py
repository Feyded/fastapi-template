from fastapi import FastAPI

from my_fastapi_app_v2.exception_handlers import app_error_handler
from my_fastapi_app_v2.exceptions import AppError
from my_fastapi_app_v2.routers import auth, task, user

app = FastAPI(title="Task Management API")

app.add_exception_handler(AppError, app_error_handler)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(task.router)


@app.get("/")
def root():
    return {"message": "Task Management API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
