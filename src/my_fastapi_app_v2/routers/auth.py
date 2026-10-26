from fastapi import APIRouter, Request, Response

from my_fastapi_app_v2.core.rate_limiter import limiter
from my_fastapi_app_v2.dependencies import DbSession
from my_fastapi_app_v2.schemas.auth import LoginResponse, UserLogin
from my_fastapi_app_v2.services import auth as auth_service

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=LoginResponse, status_code=200)
@limiter.limit("5/minute")
def login(
    request: Request,
    response: Response,
    payload: UserLogin,
    db: DbSession,
):
    user, token = auth_service.login_user(db, payload)

    return {
        "message": "User login successfully",
        "data": {"user": user, "token": token},
    }
