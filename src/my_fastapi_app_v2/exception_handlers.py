from fastapi import Request
from fastapi.responses import JSONResponse

from my_fastapi_app_v2.exceptions import AppError


async def app_error_handler(
    request: Request,
    exc: AppError,
) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message},
    )
