#Importaciones
from fastapi import FastAPI
import asyncio

#instancias: para mandar a llamar un objeto
app = FastAPI()

#Endpoints: una dirección para un recurso
@app.get("/")
async def bienvenida():
    return {"mensaje": "¡Bienvenido a mi API!"}

@app.get("/HolaMundo")
async def hola():
    await asyncio.sleep(7) # simulación de una petición
    return {
        "mensaje": "¡Hola Mundo FastAPI!",
        "estatus": "200"
           }