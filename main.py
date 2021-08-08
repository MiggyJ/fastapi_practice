from fastapi import FastAPI
from routes import userRoutes

app = FastAPI()
app.include_router(userRoutes.router)


@app.get('/')
def index():
    return {'message': 'successful app'}

