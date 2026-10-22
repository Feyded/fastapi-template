class AppError(Exception):
    """Base class for application-level errors."""

    status_code = 400

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class BadRequestError(AppError):
    """Raised when the request is invalid or malformed."""

    status_code = 400


class UnauthorizedError(AppError):
    """Raised when authentication is required or has failed."""

    status_code = 401


class ForbiddenError(AppError):
    """Raised when the user lacks permission to perform an action."""

    status_code = 403


class NotFoundError(AppError):
    """Raised when the requested resource does not exist."""

    status_code = 404


class ConflictError(AppError):
    """Raised when the request conflicts with the current resource state."""

    status_code = 409
