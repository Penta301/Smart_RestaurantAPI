import sys
import time 
sys.path.append('..')
from hashing import Hash
from fastapi import HTTPException, APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from database import authenticate_operation, collection_user
from backend.model import Token, Settings

router = APIRouter(
    prefix="/api/authentication",
    tags=['authentication']
)

@AuthJWT.load_config
def get_config():
    return Settings()

@router.post('/')
async def authenticate(user:Token, Authorize: AuthJWT = Depends()):
    response = await authenticate_operation(collection_user, user.name)
    if not response:
        raise HTTPException(404, f"That user with the email: {user.name}, doesn't exist")
    
    verify_pass = Hash.verify(user.password, response["password"])   
    
    if not verify_pass: 
        raise HTTPException(404, f"Invalid Credentials")

    access_token = Authorize.create_access_token(subject=user.name)

    return {"jwt": access_token}

@router.get("/get_csrf")
async def test(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required(csrf_token=None)
    
    msg = Authorize.get_jwt_subject()
    return {"user": msg}