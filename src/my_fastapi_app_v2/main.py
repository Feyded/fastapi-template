from fastapi import FastAPI

from my_fastapi_app_v2.database import Base, engine
from my_fastapi_app_v2.routers.tasks import router as tasks_router

app = FastAPI(title="Task Management API")

app.include_router(tasks_router, prefix="/tasks", tags=["Tasks"])

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Task Management API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
