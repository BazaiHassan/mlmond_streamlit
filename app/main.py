from fastapi import FastAPI
from .api import router

app = FastAPI()

@app.get('/')
async def read_root():
    return {
        "message": "StreamLit Learning"
    }

# Including additional routes from api.py
app.include_router(router)
