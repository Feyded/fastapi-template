from sqlalchemy import select
from sqlalchemy.orm import Session

from my_fastapi_app_v2.exceptions import NotFoundError
from my_fastapi_app_v2.models.user import User
from my_fastapi_app_v2.schemas.user import UserCreate


def list_users(db: Session) -> list[User]:
    return db.scalars(select(User)).all()


def get_user(db: Session, user_id: int) -> User:
    user = db.get(User, user_id)

    if user is None:
        raise NotFoundError("User not found.")

    return user

def create_user(db: Session, payload: UserCreate) -> User:
    user = db.get(User, user_id)

    if user is None:
        raise NotFoundError("User not found.")

    return user
