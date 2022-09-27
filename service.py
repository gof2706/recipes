# from datetime import datetime
import time
import json
from models.recipe import ReturnedRecipe
from models.user import RegisterUser, ReturnedUser, User
from pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId

# import motor.motor_asyncio

# client=motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
client= MongoClient('localhost',27017)
db = client['recipes']
users_collection=db.get_collection("users")
login_collection=db.get_collection("login")
recipe_collection=db.get_collection("recipes")

async def validate_user(auth_token):
    user = users_collection.find_one({"auth_token":auth_token})
    # print(user)
    if str(auth_token)=="123123":
        return True
    elif user==None:
        return False
    elif user["ban"]==True:
        return False
    else:
        return True

async def admin_validate(token):
    if str(token)=="123123":
        return True
    else: 
        return False

async def get_auth_token(login):
    login=login.dict()
    # print(type(login))
    # login=dict(login)
    log=dict(login_collection.find_one({"nickname":login["nickname"]}))
    print(log)
    if log["password"]==login["password"]:
        return {"auth_token":str(hash(log["password"]+log["nickname"]))}
    else: 
        return {"status":404,"msg":"Password wrong"}

async def register_user(data):
    user=dict(User.parse_obj(data))
    user["created"]=time.time()
    user["updated"]=time.time()
    # print(hash)
    users=list(users_collection.find({"nickname":user['nickname']}))
    if len(users)>0:
        return {"msg":"Nickname already in use"}
    else:
        login_collection.insert_one(data.dict())
        hash=await get_auth_token(data)
        user["auth_token"]=hash["auth_token"]
        users_collection.insert_one(user).inserted_id
        # print(str(id))
        return {"msg":"Successfully registred","auth_token":hash["auth_token"]}


async def get_user(data):
    ob=ObjectId(data)
    user=users_collection.find_one(ob)
    res= ReturnedUser.parse_obj(user)
    return res

async def get_all_users():
    users=users_collection.find({"ban":False}).sort("recipes_count",pymongo.DESCENDING).limit(10)
    res=[]
    for i in users:
        # print(i)
        alfa=ReturnedUser.parse_obj(i).dict()
        # print(type(alfa))
        alfa["id"]=str(i["_id"])
        res.append(alfa)
    return res

async def add_recipe(data):
    recipe=data.dict()
    ob=ObjectId(recipe["author"])
    users_collection.find_one_and_update({"_id":ob},{ '$inc': { "recipes_count": 1 } })
    recipe["created"]=time.time()
    res=recipe_collection.insert_one(recipe)
    return {"msg":"Success"}

async def get_recipe(data):
    ob=ObjectId(json.loads(data)["id"])
    recipe=recipe_collection.find_one(ob)
    # res=user
    return json.loads(json.dumps(recipe,default=str))

async def get_all_recipes(data):
    query=data
    print(data)
    recipes=recipe_collection.find({query["filter"]:{"$regex":query["query"]},"ban":False,}).sort(query["sort_filter"],pymongo.DESCENDING).skip((int(query["page"])-1)*2).limit(2)
    res=[]
    for i in recipes:
        # print(i)
        alfa=ReturnedRecipe.parse_obj(i).dict()
        # print(type(alfa))
        alfa["id"]=str(i["_id"])
        res.append(alfa)
    return res

async def ban_user(id):
    print(id)
    ob=ObjectId(id)
    users_collection.find_one_and_update({"_id":ob},{"$set": {"ban":True}})
    return {"status":200,"msg":"success"}

async def ban_recipe(id):
    ob=ObjectId(id)
    recipe_collection.find_one_and_update({"_id":ob},{"$set": {"ban":True}})
    return {"status":200,"msg":"success"}

async def unban_user(id):
    ob=ObjectId(id)
    users_collection.find_one_and_update({"_id":ob},{"$set": {"ban":False}})
    return {"status":200,"msg":"success"}

async def unban_recipe(id):
    ob=ObjectId(id)
    recipe_collection.find_one_and_update({"_id":ob},{"$set": {"ban":False}})
    return {"status":200,"msg":"success"}

async def delete_user(auth):
    user = users_collection.find_one({"auth_token":auth})
    # print(str(user))
    recipe_collection.delete_many({"author":str(user["_id"])})
    users_collection.find_one_and_delete({"_id":user["_id"]})
    return {"status" :200}


async def delete_recipe(id,auth):
    # print(str(user))
    user = users_collection.find_one({"auth_token":auth})
    ob= ObjectId(id)
    recipe_collection.find_one_and_delete({"_id":ob,"author":str(user["_id"])})
    return {"status" :200}


