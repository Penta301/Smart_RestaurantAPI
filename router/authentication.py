import sys
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
    refresh_token = Authorize.create_refresh_token(subject=user.name)

    Authorize.set_access_cookies(access_token)
    Authorize.set_refresh_cookies(refresh_token)

    msg = Authorize.get_raw_jwt()
    return {"msg": 'Successfully Login'}

@router.get("/get_jwt")
async def test(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    
    msg = Authorize.get_raw_jwt()
    return {"crf": msg['csrf']}