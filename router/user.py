import sys
sys.path.append('..')
from fastapi import HTTPException, APIRouter
from hashing import Hash
from backend.model import User, ShowUser
from backend.database import (
    collection_user, 
    create_operation,
)

router = APIRouter(
    prefix="/api",
    tags=['User']
)

@router.post("/create_user/", response_model = ShowUser)
async def post_todo(user: User):
    user = user.dict()
    user["password"] = Hash.encrypt(user["password"])
    print(user)
    response = await create_operation(user, collection_user)
    if response == "error_name":
        raise HTTPException(400, "That username exist")
    if response:
        return response
    raise HTTPException(400, "Something went wrong")
