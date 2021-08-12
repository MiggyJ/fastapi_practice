from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from routes import authRoutes, userRoutes, postRoutes
from database import get_db
from models.postModel import Post

# Register template folder
template = Jinja2Templates('templates')

app = FastAPI()
# Mount static folder
app.mount('/static', StaticFiles(directory='static'), name='static')

# Register Routes
app.include_router(authRoutes.router)
app.include_router(userRoutes.router)
app.include_router(postRoutes.router)

@app.get('/', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    try:
        posts = db.query(Post).all()
        return template.TemplateResponse('index.html', {
            'request': request,
            'posts': posts
        })
    except Exception as e:
        print(e)

