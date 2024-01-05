from typing import Optional, Annotated

from pydantic import BaseModel, Field, EmailStr, StringConstraints


class User(BaseModel):
    username: str
    age: Annotated[int, Field(gt=18)]
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length=8, max_length=16)]
    phone: Optional[str] = "Unknown"


class User_registration(BaseModel):
    username: str
    password: str
