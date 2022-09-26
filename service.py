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

async def get_auth_token():
    pass

async def register_user(data):
    user=dict(User.parse_obj(data))
    users=list(users_collection.find({"nickname":user['nickname']}))
    # print(users)
    if len(users)>0:
        return {"msg":"Nickname already in use"}
    else:
        login_collection.insert_one(data.dict())
        users_collection.insert_one(user)
        return {"msg":"Successfully registred"}


async def get_user(data):
    # user=data.dict()
    ob=ObjectId("6331aad61b8553c9ea7e8a21")
    user=users_collection.find_one(ob)
    # res=user
    return json.loads(json.dumps(user,default=str))

