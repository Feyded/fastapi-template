from typing import Annotated

import jwt
from fastapi import Depends
from jwt.exceptions import InvalidTokenError
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import ALGORITHM, AccessToken
from app.core.settings import settings
from app.exceptions import ForbiddenError, UnauthorizedError
from app.features.users.model import User

DbSession = Annotated[Session, Depends(get_db)]


def get_current_user(
    token: AccessToken,
    db: DbSession,
) -> User:

    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[ALGORITHM],
        )

        subject = payload.get("sub")

        if subject is None:
            raise InvalidTokenError("Missing subject")

        user_id = int(subject)

    except InvalidTokenError, TypeError, ValueError:
        raise UnauthorizedError("Could not validate credentials")

    user = db.get(User, user_id)

    if user is None:
        raise UnauthorizedError("Could not validate credentials")

    return user


CurrentUser = Annotated[User, Depends(get_current_user)]


def require_role(allowed_roles: list[str]):
    def role_checker(
        current_user: CurrentUser,
    ) -> User:
        if current_user.role not in allowed_roles:
            raise ForbiddenError("You do not have permission to access this resource")

        return current_user

    return role_checker
