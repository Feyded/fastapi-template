from fastapi import status


class AppError(Exception):
    """Base class for application-level errors."""

    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class BadRequestError(AppError):
    """Raised when the request is invalid or malformed."""

    status_code = status.HTTP_400_BAD_REQUEST


class UnauthorizedError(AppError):
    """Raised when authentication is required or has failed."""

    status_code = status.HTTP_401_UNAUTHORIZED


class ForbiddenError(AppError):
    """Raised when the user lacks permission to perform an action."""

    status_code = status.HTTP_403_FORBIDDEN


class NotFoundError(AppError):
    """Raised when the requested resource does not exist."""

    status_code = status.HTTP_404_NOT_FOUND


class ConflictError(AppError):
    """Raised when the request conflicts with the current resource state."""

    status_code = status.HTTP_409_CONFLICT
