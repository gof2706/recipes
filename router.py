from fastapi import APIRouter
from models.recipe import Recipe
from models.user import RegisterUser, User
import service

router=APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get('/get_all_users')
async def get_users():
    pass

@router.get('/get_all_recipes')
async def get_recipes():
    pass

@router.get('/get_user')
async def get_user(id):
    pass

@router.get('/get_recipe')
async def get_recipe(id):
    pass


@router.post('/register_user')
async def register(data:RegisterUser):
    return await service.register_user(data)

@router.post('/add_user')
async def add_user(user:User):
    print(user.dict())
    # us=client
    return user

@router.post('/add_recipe')
async def add_recipes(recipe):
    pass

@router.put('/update_user')
async def update_user():
    pass

@router.put('/update_recipe')
async def update_recipe():
    pass

@router.delete('/delete_user')
async def delete_user():
    pass

@router.delete('/delete_recipe')
async def delete_recipe():
    pass

@router.delete('/delete_all_users')
async def delete_all_users():
    pass

@router.delete('/delete_all_recipes')
async def delete_all_recipes():
    pass