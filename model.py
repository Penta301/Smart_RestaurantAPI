from pydantic import BaseModel
from typing import ByteString, Optional

class Food(BaseModel):
    name:str
    price:int
    available:Optional[bool] = True
    cantidad: Optional[int] = None
    delay: Optional[int] = None
    desc: Optional[str] = None

class Request(BaseModel):
    table:int
    food:list
    account:int

class User(BaseModel):
    name:str
    password:str
    service:str
    paid:int
    restaurant:Optional[list] = None

class ShowUser(BaseModel):
    name:str
    restaurant:list

class Restaurant(BaseModel):
    name:str
    tables: Optional[int] = None 
    food: Optional[list] = None
    requests: Optional[list] = None

class Show_Restaurant(BaseModel):
    name:str
    tables: Optional[int] = None
    food: Optional[list] = None
    requests: Optional[list] = None

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    email:Optional[str] = None

