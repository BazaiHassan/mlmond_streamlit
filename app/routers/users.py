from fastapi import APIRouter

router = APIRouter()

@router.post('/register')
async def user_register():
    ...


@router.post('/login')
async def user_login():
    ...

@router.post('/forget-password')
async def user_forget_password():
    ...

@router.post('/email-verification')
async def user_email_verification():
    ...

@router.get('/profile')
async def user_profile():
    ...

@router.put('/update-profile')
async def user_update_profile():
    ...