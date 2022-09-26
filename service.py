from datetime import datetime
import json
from models.user import RegisterUser, User
from pymongo import MongoClient
from bson.objectid import ObjectId
# import motor.motor_asyncio

# client=motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
client= MongoClient('localhost',27017)
db = client['recipes']
users_collection=db.get_collection("users")
login_collection=db.get_collection("login")
recipe_collection=db.get_collection("recipes")

async def get_auth_token():
    pass

async def register_user(data):
    user=dict(User.parse_obj(data))
    user["created"]=datetime.now()
    users=list(users_collection.find({"nickname":user['nickname']}))
    # print(users)
    if len(users)>0:
        return {"msg":"Nickname already in use"}
    else:
        login_collection.insert_one(data.dict())
        id=users_collection.insert_one(user).inserted_id
        # print(str(id))
        return {"msg":"Successfully registred "}


async def get_user(data):
    # user=data.dict()
    ob=ObjectId(json.loads(data)["id"])
    user=users_collection.find_one(ob)
    # res=user
    return json.loads(json.dumps(user,default=str))

async def add_recipe(data):
    recipe=data.dict()
    recipe["created"]=datetime.now()
    res=recipe_collection.insert_one(recipe)
    return {"msg":"Success"}

async def get_recipe(data):
    ob=ObjectId(json.loads(data)["id"])
    recipe=recipe_collection.find_one(ob)
    # res=user
    return json.loads(json.dumps(recipe,default=str))

async def get_all_recipes():
    pass


