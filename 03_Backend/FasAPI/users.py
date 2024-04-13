from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    age : int
    alias: str

users_list = [User(id = 1, name = 'Nacho', surname = 'Sanson', age = 33, alias = 'Sanson'),
        User(id = 2, name = 'Nuria', surname = 'Soriano', age = 30, alias = 'Nur'),
         User(id = 3, name = 'David', surname = 'Izquierdo', age = 34, alias = 'El corredr')]

@app.get('/users')
async def users():
    return users_list

@app.get('/user/{id}')
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    return list(users)