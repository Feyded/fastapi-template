from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=100)


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


class UserSingleResponse(BaseModel):
    message: str
    data: UserResponse


class UserListResponse(BaseModel):
    message: str
    data: list[UserResponse]
