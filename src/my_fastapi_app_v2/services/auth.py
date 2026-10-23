from sqlalchemy import select
from sqlalchemy.orm import Session

from my_fastapi_app_v2.core.security import create_access_token, verify_password
from my_fastapi_app_v2.exceptions import UnauthorizedError
from my_fastapi_app_v2.models.user import User
from my_fastapi_app_v2.schemas.auth import UserLogin


def login_user(db: Session, payload: UserLogin) -> tuple[User, str]:
    user = db.scalar(select(User).where(User.email == payload.email))

    if user is None or not verify_password(payload.password, user.hashed_password):
        raise UnauthorizedError("Invalid email or password")

    token = create_access_token(subject=str(user.id))

    return user, token
