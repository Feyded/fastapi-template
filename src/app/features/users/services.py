from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.exceptions import ConflictError, NotFoundError
from app.features.users.model import User
from app.features.users.schemas import UserCreate


def list_users(db: Session, page: int = 1, limit: int = 10) -> list[User]:
    offset = (page - 1) * limit
    statement = select(User).offset(offset).limit(limit)
    return db.scalars(statement).all()


def get_user(db: Session, user_id: int) -> User:
    user = db.get(User, user_id)

    if user is None:
        raise NotFoundError("User not found.")

    return user


def create_user(db: Session, payload: UserCreate) -> User:
    existing_user = db.scalar(select(User).where(User.email == payload.email))

    if existing_user is not None:
        raise ConflictError("A user with this email already exists.")

    user_data = payload.model_dump(exclude=["password"])
    user_data["hashed_password"] = hash_password(payload.password)

    user = User(**user_data)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
