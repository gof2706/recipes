from pydantic import BaseModel
import datetime
from bson import ObjectId

class User(BaseModel):
    nickname:str
    ban:bool | None = False
    favorites:list[str] | None = []
    created:float | None=None
    updated:float | None=None
    auth_token:str | None = None
    recipes_count:int | None = 0

class RegisterUser(BaseModel):
    nickname:str
    password:str

class Validate(BaseModel):
    auth_token:str

class ReturnedUser(BaseModel):
    nickname:str
    ban:bool | None = False
    favorites:list[str] | None = []
    created:float | None=None
    updated:float | None=None
    recipes_count:int | None = 0
    class Config:
        orm_mode = True
