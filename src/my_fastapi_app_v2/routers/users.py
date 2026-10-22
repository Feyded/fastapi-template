from fastapi import APIRouter

from my_fastapi_app_v2.dependencies import DbSession
from my_fastapi_app_v2.schemas.user import UserCreate
from my_fastapi_app_v2.services import users as user_service

router = APIRouter(prefix="users", tags=["Users"])


@router.get("/")
def list_users(db: DbSession):
    users = user_service.list_users(db)

    return {
        "message": "Users retrieved successfully",
        "data": users,
    }


@router.get("/{user_id}")
def get_user(
    user_id: int,
    db: DbSession,
):
    user = user_service.get_user(db, user_id)

    return {
        "message": "User created successfully",
        "data": user,
    }


@router.post("/")
def create_user(
    user_data: UserCreate,
    db: DbSession,
):
    user = user_service.create_user(db, user_data)

    return {
        "message": "User created successfully",
        "data": user,
    }
