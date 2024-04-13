from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return '¡Hola FastAPI!'

@app.get('/nombre')
async def nombre():
    return{'Nombre':'Nacho', 'Apellido':'Sansón', 'Edad':33 , 'Altura':1.78}

# Iniciar el server: uvicorn main:app --reload
#Documentación con Swagger: /docs
#Documentación con Redocly: /redoc