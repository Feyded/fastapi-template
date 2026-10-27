from pydantic import BaseModel, EmailStr, Field

from app.features.users.schemas import UserResponse


class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1)


class LoginData(BaseModel):
    user: UserResponse
    token: str


class LoginResponse(BaseModel):
    message: str
    data: LoginData
