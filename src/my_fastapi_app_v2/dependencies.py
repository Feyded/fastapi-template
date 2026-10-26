from typing import Annotated

import jwt
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt.exceptions import InvalidTokenError
from sqlalchemy.orm import Session

from my_fastapi_app_v2.core.security import ALGORITHM
from my_fastapi_app_v2.core.settings import settings
from my_fastapi_app_v2.database import get_db
from my_fastapi_app_v2.exceptions import ForbiddenError, UnauthorizedError
from my_fastapi_app_v2.models.user import User

DbSession = Annotated[Session, Depends(get_db)]

bearer_scheme = HTTPBearer()


def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(bearer_scheme)],
    db: DbSession,
) -> User:
    token = credentials.credentials

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
