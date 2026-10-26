from datetime import UTC, datetime, timedelta

import jwt
from pwdlib import PasswordHash

from app.core.settings import settings

ALGORITHM = "HS256"

password_hash = PasswordHash.recommended()


def create_access_token(
    subject: str,
    expires_minutes: int = 30,
) -> str:
    expires_at = datetime.now(UTC) + timedelta(minutes=expires_minutes)

    payload = {
        "sub": subject,
        "exp": expires_at,
    }

    return jwt.encode(
        payload,
        settings.secret_key,
        algorithm=ALGORITHM,
    )


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    return password_hash.verify(
        plain_password,
        hashed_password,
    )
