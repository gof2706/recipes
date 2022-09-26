from fastapi import FastAPI
from pymongo import MongoClient
import router

app = FastAPI()
app.include_router(router.router)
client=MongoClient('localhost', 27017)

