from fastapi import APIRouter, Body
from .models import CreatePostIn
router = APIRouter()

@router.get('/additional')
async def additional_route():
    return {"message": "This is an additional route"}

@router.post('/create')
async def create_post(post: CreatePostIn = Body()):
    return post

