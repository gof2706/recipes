import string
from fastapi import FastAPI
import pymongo
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/get_all_users')
async def get_users():
    pass

@app.get('/get_all_recipes')
async def get_recipes():
    pass

@app.get('/get_user')
async def get_user():
    pass

@app.get('/get_recipe')
async def get_recipe():
    pass

@app.post('/add_user')
async def get_recipes(user):
    pass

@app.post('/add_recipe')
async def get_recipes(recipe):
    pass

@app.put('/update_user')
async def update_user():
    pass

@app.put('/update_recipe')
async def update_recipe():
    pass

@app.delete('/delete_user')
async def delete_user():
    pass

@app.delete('/delete_recipe')
async def delete_recipe():
    pass

@app.delete('/delete_all_users')
async def delete_all_users():
    pass

@app.delete('/delete_all_recipes')
async def delete_all_recipes():
    pass