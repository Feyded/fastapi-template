from fastapi import APIRouter, Request, Response

from app.core.rate_limiter import limiter
from app.schemas.auth import LoginResponse, UserLogin
from app.services import auth as auth_service
from src.app.dependencies import DbSession

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=LoginResponse)
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
