from fastapi import FastAPI
from routes import userRoutes, postRoutes

from database import Base, engine

#* Generate (Automatic) Tables from SQLAlchemy models
#* Must drop tables for updates
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(userRoutes.router)


@app.get('/')
def index():
    return {'message': 'successful app'}

