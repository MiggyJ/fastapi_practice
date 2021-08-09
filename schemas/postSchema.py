from datetime import datetime as dt
from pydantic import BaseModel

class PostBase(BaseModel):
    id: int
    author_id: int
    title: str
    body: str

class CreatePost(PostBase):
    pass

class Post(PostBase):
    created_at: dt
    updated_at: dt