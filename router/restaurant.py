import sys
sys.path.append('..')
from backend.oauth2 import get_current_user
from fastapi import HTTPException, APIRouter, Depends
from hashing import Hash
from backend.model import Restaurant, Show_Restaurant, User
from backend.database import (
    collection_restaurant, 
    fetch_all,
    create_operation,
    update_operation,
    remove_operation
)

router = APIRouter(
    prefix="/api",
    tags=['Restaurant']
)

@router.get("/get_all_restaurants/")
async def get_all_operations(get_current_user:User = Depends(get_current_user)):
    response = await fetch_all(collection_restaurant, Show_Restaurant)
    return response

@router.post("/restaurant_create/", response_model = Show_Restaurant)
async def post_todo(restaurant: Restaurant, get_current_user:User = Depends(get_current_user)):
    restaurant = restaurant.dict()
    response = await create_operation(restaurant, collection_restaurant)
    if response == "error_name":
        raise HTTPException(400, "That username exist")
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@router.put("/restaurant_edit/{name}/")
async def edit_operation(name:str, restaurant:Restaurant, get_current_user:User = Depends(get_current_user)):
    response = await update_operation(collection_restaurant, name, restaurant.dict())
    if response:
        return "Succesfully edited"
    raise HTTPException(404, f"That restaurant with the name: {name}, doesn't exist")

@router.delete("/restaurant_delete/{name}/")
async def delete_operation(name, get_current_user:User = Depends(get_current_user)):
    response = await remove_operation(collection_restaurant, name)
    if response:
        return "Succesfully deleted operation"
    raise HTTPException(404, f"That restaurant with the name: {name}, doesn't exist")