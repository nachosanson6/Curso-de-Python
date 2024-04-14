from fastapi import FastAPI,HTTPException

app = FastAPI()


@app.get('/proeudcts')
async def products():
    return ['Producto 1','Producto 2','Producto 3','Producto 4','Producto 5']