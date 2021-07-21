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
    csrf_token: str

class Show_Restaurant(BaseModel):
    name:str
    tables: Optional[int] = None
    food: Optional[list] = None
    requests: Optional[list] = None

class Token(BaseModel):
    name:str
    password:str

class Settings(BaseModel):
   authjwt_secret_key: str = '7b82e1d300da121b2470deb960b1b802022607de6bf71816123c0d7742fa5f48'
   authjwt_access_token_expires: int = 3600
   authjwt_token_location: set = ('headers', "cookies")
   authjwt_cookie_secure: bool = False
   authjwt_cookie_csrf_protect: bool = True
   authjwt_access_csrf_cookie_key='csrf_access_token'