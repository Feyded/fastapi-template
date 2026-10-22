from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str = Field(min_lenght=2, max_lenght=100)
    email: EmailStr
