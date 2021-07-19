import sys
sys.path.append('..')
from hashing import Hash
from fastapi import HTTPException, APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from database import authenticate_operation, collection_user
from backend.JWTtoken import create_access_token

router = APIRouter(
    prefix="/api/authentication",
    tags=['authentication']
)

@router.post('/')
async def authenticate(user:OAuth2PasswordRequestForm = Depends()):
    response = await authenticate_operation(collection_user, user.username)
    if not response:
        raise HTTPException(404, f"That user with the email: {user.username}, doesn't exist")
    
    verify_pass = Hash.verify(user.password, response["password"])   
    
    if not verify_pass: 
        raise HTTPException(404, f"Invalid Credentials")

    access_token = create_access_token(data={"sub": user.username})

    access_token = {"access_token": access_token, "token_type": "bearer"}

    return_response = JSONResponse(content=access_token)

    return_response.set_cookie(key='JWTOKEN', value=access_token, httponly=True, max_age=3600)

    return return_response