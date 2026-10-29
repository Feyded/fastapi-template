from fastapi import APIRouter, Request, Response

from app.core import settings
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

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=settings.cookie_secure,
        samesite="lax",
        max_age=60 * 60,  # 1 hour
        path="/",
    )

    return {
        "message": "User login successfully",
        "data": user,
    }


@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(
        key="access_token",
        path="/",
        httponly=True,
        secure=settings.cookie_secure,
        samesite="lax",
    )

    return {"message": "Logged out successfully"}
