from fastapi import APIRouter
from models.recipe import Recipe
from models.user import RegisterUser, ReturnedUser, User, Validate
import service

router=APIRouter()


@router.get('/get_ten_users')############
async def get_users(auth_token:str):
    if await service.validate_user(auth_token):
        return await service.get_all_users()

    else:
        return {"status":401,"msg":"Wrong Auth token or your account in ban"}
    # pass

@router.get('/get_all_recipes')############
async def get_recipes(auth_token:str,filter='name',sort_filter='name',page=1,query=""):
    if await service.validate_user(auth_token):
        return await service.get_all_recipes({'filter':filter,"sort_filter":sort_filter,"page":page,"query":query})
    else:
        return {"status":401,"msg":"Wrong Auth token or your account in ban"}

@router.get('/get_user')############
async def get_user(id,auth_token:str):
    if await service.validate_user(auth_token):
        return await service.get_user(id)
    else:
        return {"status":401,"msg":"Wrong Auth token or your account in ban"}

@router.get('/get_recipe')############
async def get_recipe(id,auth_token:str):
    if await service.validate_user(auth_token):
        return await service.get_recipe(id)
    else:
        return {"status":401,"msg":"Wrong Auth token or your account in ban"}


@router.post('/register_user')
async def register(data:RegisterUser):
    return await service.register_user(data)
    

@router.post('/login')
async def login(data:RegisterUser):
    return await service.get_auth_token(data)

@router.post('/add_recipe')############
async def add_recipes(recipe:Recipe,auth_token:str):
    if await service.validate_user(auth_token):
        return await service.add_recipe(recipe)
    else:
        return {"status":401,"msg":"Wrong Auth token or your account in ban"}

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

@router.put('/ban_user')
async def ban_user(ban_id,token):
    # print(ban_id,token)
    if await service.admin_validate(token):
        # print('im here')
        return await service.ban_user(ban_id)
    else:
        return {"status":401,"msg":"You are not admin"}

@router.put('/ban_recipe')
async def ban_user(ban_id,token):
    
    if await service.admin_validate(token):
        return await service.ban_recipe(ban_id)
    else:
        return {"status":401,"msg":"You are not admin"}

@router.put('/unban_user')
async def unban_user(ban_id,token):
    if await service.admin_validate(token):
        return await service.unban_user(ban_id)
    else:
        return {"status":401,"msg":"You are not admin"}

@router.put('/unban_recipe')
async def unban_user(ban_id,token):
    if await service.admin_validate(token):
        return await service.unban_recipe(ban_id)
    else:
        return {"status":401,"msg":"You are not admin"}