from pydantic import BaseModel, EmailStr, Field

from my_fastapi_app_v2.schemas.user import UserResponse


class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1)


class LoginData(BaseModel):
    user: UserResponse
    token: str


class LoginResponse(BaseModel):
    message: str
    data: LoginData
