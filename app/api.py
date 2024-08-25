from fastapi import APIRouter

router = APIRouter()

@router.get('/additional')
async def additional_route():
    return {"message": "This is an additional route"}
