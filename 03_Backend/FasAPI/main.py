# Iniciar el server: uvicorn main:app --reload
# Documentación con Swagger: /docs
# Documentación con Redocly: /redoc
# Arrancar myenv: source myenv/bin/activate


from fastapi import FastAPI
from routes import products,users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#routes
app.include_router(products.router)
app.include_router(users.router)
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get('/')
async def root():
    return '¡Hola FastAPI!'

@app.get('/nombre')
async def nombre():
    return{'Nombre':'Nacho', 'Apellido':'Sansón', 'Edad':33 , 'Altura':1.78}


