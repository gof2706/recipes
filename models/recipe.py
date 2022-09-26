from pydantic import BaseModel
import datetime

class Recipe(BaseModel):
    author:str
    created:datetime.time
    updated:datetime.time
    name:str
    recipe_type:str
    description:str
    guide:list[str]
    img_url:str
    tags:list[str]
    ban:bool