from fastapi import APIRouter,HTTPException
from pydantic import BaseModel

router = APIRouter(prefix='/users',tags=['users'],responses={404:{'message':'No encontrado'}})

class User(BaseModel):
    id: int
    name: str
    surname: str
    age : int
    alias: str

users_list = [User(id = 1, name = 'Nacho', surname = 'Sanson', age = 33, alias = 'Sanson'),
        User(id = 2, name = 'Nuria', surname = 'Soriano', age = 30, alias = 'Nur'),
         User(id = 3, name = 'David', surname = 'Izquierdo', age = 34, alias = 'El corredr')]

@router.get('/')
async def users():
    return users_list

### Path
@router.get('/{id}')  # http://localhost:8000/user/2
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try :
        return list(users)[0]
    except:
        return "{'error':'No se he encontrado el usuario}"
    

### Query
@router.get('/userquery/')  # http://localhost:8000/userquery/?id=1
async def user(id: int):
  return search_user(id)
    


@router.post('/new_user',response_model=User,status_code=201)
async def user(user : User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404,detail='El usuario ya existe')
        

    users_list.append(user)
    return user


@router.put('/')
async def user(user:User):
    for index,saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user


@router.delete('/delete_user/{id}')
async def user(id:int):
    for index,saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            return (' Usuario eliminado')


def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try :
        return list(users)[0]
    except:
        return "{'error':'No se he encontrado el usuario}"



