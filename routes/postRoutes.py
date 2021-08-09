from fastapi import APIRouter
from schemas.postSchema import CreatePost
from models.postModel import Post
from database import get_db

router = APIRouter(
    prefix='/posts',
    tags=['posts']
)

