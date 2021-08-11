from datetime import datetime as dt
from pydantic import BaseModel

class PostBase(BaseModel):
    id: int
    author_id: int
    title: str
    body: str

# Schema for request body
class CreatePost(PostBase):
    pass

#Schema for response body
class Post(PostBase):
    created_at: dt
    updated_at: dt