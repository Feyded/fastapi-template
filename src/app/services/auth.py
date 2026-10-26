from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import create_access_token, verify_password
from app.exceptions import UnauthorizedError
from app.models.user import User
from app.schemas.auth import UserLogin


def login_user(db: Session, payload: UserLogin) -> tuple[User, str]:
    user = db.scalar(select(User).where(User.email == payload.email))

    if user is None or not verify_password(payload.password, user.hashed_password):
        raise UnauthorizedError("Invalid email or password")

    token = create_access_token(subject=str(user.id))

    return user, token
