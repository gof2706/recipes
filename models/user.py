from pydantic import BaseModel
import datetime

class User(BaseModel):
    nickname:str
    ban:bool | None = False
    favorites:list[str] | None = []
    created:datetime.time | None=None
    updated:datetime.time | None=None
    acess_token:str | None = None

class RegisterUser(BaseModel):
    nickname:str
    password:str

