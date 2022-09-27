from pydantic import BaseModel
import datetime

class Recipe(BaseModel):
    author:str
    created:int | None = None
    updated:int | None = None
    name:str | None = None
    recipe_type:str | None = None
    description:str | None = None
    guide:list[str] | None = None
    img_url:str | None = None
    tags:list[str] | None = None
    ban:bool | None = False
    likes:int | None = 0

class ReturnedRecipe(BaseModel):
    author:str
    created:int | None = None
    updated:int | None = None
    name:str | None = None
    recipe_type:str | None = None
    description:str | None = None
    img_url:str | None = None
    tags:list[str] | None = None
    ban:bool | None = False
    likes:int | None = 0