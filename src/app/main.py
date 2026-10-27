from fastapi import FastAPI
from slowapi.errors import RateLimitExceeded
from slowapi.extension import _rate_limit_exceeded_handler
from slowapi.middleware import SlowAPIMiddleware

from app.core.rate_limiter import limiter
from app.exception_handlers import app_error_handler
from app.exceptions import AppError
from app.features.auth import router
from app.features.tasks import router
from app.features.users import router

app = FastAPI(title="Task Management API")

app.state.limiter = limiter

app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler,
)
app.add_exception_handler(AppError, app_error_handler)

app.add_middleware(SlowAPIMiddleware)

app.include_router(router.router)
app.include_router(router.router)
app.include_router(router.router)


@app.get("/")
def root():
    return {"message": "Task Management API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
