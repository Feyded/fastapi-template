from fastapi import APIRouter, Query, status

from app.dependencies import DbSession
from app.features.users import services as user_service
from app.features.users.schemas import (
    UserCreate,
    UserListResponse,
    UserSingleResponse,
)

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=UserListResponse, status_code=status.HTTP_200_OK)
def list_users(
    db: DbSession,
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=10, le=100),
):
    users = user_service.list_users(db, page, limit)

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
