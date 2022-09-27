from fastapi import APIRouter
from models.recipe import Recipe
from models.user import RegisterUser, ReturnedUser, User
import service

router=APIRouter()


@router.get('/get_ten_users',description="Возвращает 10 аккаунтов отсортированных по количеству рецептов")############
async def get_users(auth_token:str):
    if await service.validate_user(auth_token):
        return await service.get_all_users()

    else:
        return {"status":401,"msg":"Wrong Auth token or your account in ban"}
    # pass

@router.get('/get_all_recipes', description="""
Возвращает все рецепты, 
на вход поступает четыре параметра:
1) Фильтр по полю для поиска совпадений
2) Фильтр сортировки
3) Поисковый запрос
4) Cтраница пагинации""")
async def get_recipes(auth_token:str,filter='name',sort_filter='name',page=1,query=""):
    if await service.validate_user(auth_token):
        return await service.get_all_recipes({'filter':filter,"sort_filter":sort_filter,"page":page,"query":query})
    else:
        return {"status":401,"msg":"Wrong Auth token or your account in ban"}

@router.get('/get_user', description="""
Возвращает пользователя по его id
""")############
async def get_user(id,auth_token:str):
    if await service.validate_user(auth_token):
        return await service.get_user(id)
    else:
        return {"status":401,"msg":"Wrong Auth token or your account in ban"}

@router.get('/get_recipe', description="""
Возвращает рецепт по id
""")############
async def get_recipe(id,auth_token:str):
    if await service.validate_user(auth_token):
        return await service.get_recipe(id)
    else:
        return {"status":401,"msg":"Wrong Auth token or your account in ban"}


@router.post('/register_user',description="""
Регистрация пользователя
""")
async def register(data:RegisterUser):
    return await service.register_user(data)
    

@router.post('/login',description="""
Получение кода авторизации, который используется при всех запросах кроме регистрации и авторизации
""")
async def login(data:RegisterUser):
    return await service.get_auth_token(data)

@router.post('/add_recipe',description="""
Добавление рецепта
""")############
async def add_recipes(recipe:Recipe,auth_token:str):
    if await service.validate_user(auth_token):
        return await service.add_recipe(recipe)
    else:
        return {"status":401,"msg":"Wrong Auth token or your account in ban"}


@router.put('/ban_user',description="""
Функция администратора - забанить пользователя 
""")
async def ban_user(ban_id,token):
    # print(ban_id,token)
    if await service.admin_validate(token):
        # print('im here')
        return await service.ban_user(ban_id)
    else:
        return {"status":401,"msg":"You are not admin"}

@router.put('/ban_recipe',description="""
Функция администратора - забанить рецепт 
""")
async def ban_user(ban_id,token):
    
    if await service.admin_validate(token):
        return await service.ban_recipe(ban_id)
    else:
        return {"status":401,"msg":"You are not admin"}

@router.put('/unban_user',description="""
Функция администратора - разьанить пользователя 
""")
async def unban_user(ban_id,token):
    if await service.admin_validate(token):
        return await service.unban_user(ban_id)
    else:
        return {"status":401,"msg":"You are not admin"}

@router.put('/unban_recipe',description="""
Функция администратора - разьанить рецепт 
""")
async def unban_user(ban_id,token):
    if await service.admin_validate(token):
        return await service.unban_recipe(ban_id)
    else:
        return {"status":401,"msg":"You are not admin"}

@router.delete('/delete_user',description="""
Удаление своего аккаунта
""")
async def delete_user(auth_token:str):
    if await service.validate_user(auth_token):
        return await service.delete_user(auth_token)
    else:
        return {"status":404}

@router.delete('/delete_recipe',description="""
Удаление своего рецепта
""")#######################
async def delete_recipe(id:str,auth_token:str):
    if await service.validate_user(auth_token):
        return await service.delete_recipe(id,auth_token)
    else:
        return {"status":404}