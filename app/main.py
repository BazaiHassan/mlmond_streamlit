from fastapi import FastAPI
from .routers.users import router as user_routes

app = FastAPI()

app.include_router(user_routes, prefix='/user')

