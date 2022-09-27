from fastapi import APIRouter
from models.recipe import Recipe
from models.user import RegisterUser, ReturnedUser, User, Validate
import service

router=APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get('/get_ten_users')############
async def get_users(validate):
    return await service.get_all_users()
    # pass

@router.get('/get_all_recipes')############
async def get_recipes():
    pass

@router.get('/get_user')############
async def get_user(id,access_token):
    return await service.get_user(id)

@router.get('/get_recipe')############
async def get_recipe(id):
    return await service.get_recipe(id)


@router.post('/register_user')
async def register(data:RegisterUser):
    return await service.register_user(data)

@router.post('/login')
async def login(data:RegisterUser):
    return await service.get_auth_token(data)

@router.post('/add_recipe')############
async def add_recipes(recipe:Recipe,access_token:str):
    return await service.add_recipe(recipe)

@router.put('/update_user')
async def update_user():
    pass


@router.delete('/delete_user')
async def delete_user():
    pass

@router.delete('/delete_recipe')#######################
async def delete_recipe():
    pass

@router.delete('/delete_all_users')############
async def delete_all_users():
    pass

@router.delete('/delete_all_recipes')############
async def delete_all_recipes():
    pass