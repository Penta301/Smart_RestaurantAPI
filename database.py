import motor.motor_asyncio 
from datetime import datetime 
from model import Food, Request, Restaurant


client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.Restaurant
collection_restaurant = database.restaurant
collection_food = database.restaurant_food 
collection_request = database.restaurant_request
collection_user = database.user

async def fetch_all(collection, model):
    operations=[]
    cursor = collection.find({})
    async for document in cursor:
        operations.append(model(**document))
    return operations

async def create_operation(model, collection, verify = False):
    document = model

# Revisar si existe el usuario

    try:    
        if verify:
            
            user = await collection.find_one({"name":document["name"]})
            if user:
                return "error_name"

    except AssertionError as error:
        print(error)

    result = await collection.insert_one(document)
    return document

async def update_operation(collection, name, model):
    document = model
    result = await collection.update_one({"name":name},
    {"$set":document}) 
    return result.matched_count

async def remove_operation(collection, name):
   result = await collection.delete_one({"name":name})
   return result.deleted_count

async def authenticate_operation(collection, name):
    verification_name = await collection.find_one({"name":name,})
    return verification_name