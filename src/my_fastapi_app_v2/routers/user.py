from fastapi import APIRouter, status

from my_fastapi_app_v2.dependencies import DbSession
from my_fastapi_app_v2.schemas.user import UserCreate, UserSingleResponse
from my_fastapi_app_v2.services import user as user_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", status_code=status.HTTP_200_OK)
def list_users(db: DbSession):
    users = user_service.list_users(db)

    return {
        "message": "Users retrieved successfully",
        "data": users,
    }


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
def get_user(
    user_id: int,
    db: DbSession,
):
    user = user_service.get_user(db, user_id)

    return {
        "message": "User created successfully",
        "data": user,
    }


@router.post(
    "/", response_model=UserSingleResponse, status_code=status.HTTP_201_CREATED
)
def create_user(
    payload: UserCreate,
    db: DbSession,
):
    user = user_service.create_user(db, payload)

    return {
        "message": "User created successfully",
        "data": user,
    }
