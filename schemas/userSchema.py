from datetime import datetime as dt
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    age: int

class CreateUser(UserBase):
    pass

class User(BaseModel):
    created_at: dt
    updated_at: dt