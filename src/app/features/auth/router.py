from fastapi import APIRouter, Request, Response

from app.core.rate_limiter import limiter
from app.dependencies import DbSession
from app.features.auth import services as auth_service
from app.features.auth.schemas import LoginResponse, UserLogin

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
