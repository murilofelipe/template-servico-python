# src/users/user_schemas.py
from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    username: str
    email: str


class UserInput(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
