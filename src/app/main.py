from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi.extension import _rate_limit_exceeded_handler
from slowapi.middleware import SlowAPIMiddleware

from app.core.rate_limiter import limiter
from app.exception_handlers import app_error_handler
from app.exceptions import AppError
from app.features.auth import router as auth_router
from app.features.tasks import router as task_router
from app.features.users import router as user_router

app = FastAPI(title="FastAPI Template")

app.state.limiter = limiter

app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler,
)
app.add_exception_handler(AppError, app_error_handler)

app.add_middleware(SlowAPIMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(task_router)
app.include_router(user_router)


@app.get("/")
def root():
    return {"message": "FastAPI Template is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
