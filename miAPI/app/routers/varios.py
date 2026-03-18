#Endpoints varios
import asyncio
from typing import Optional
from app.data.database import usuarios
from fastapi import APIRouter

router= APIRouter(tags=['Varios'])


@router.get("/")  # Endpoint de inicio, todos los endpoints se acompañan de una función
async def bienvenida():
    return {"mensaje": "¡Bienvenido a mi API!"}  # Formato JSON

@router.get("/HolaMundo")  # Endpoint
async def hola():
    await asyncio.sleep(7)#Simulacion de uns 
    return {"mensaje": "¡Hola Mundo FastAPI!",
            "estatus":"200"
            }  # Formato JSON

@router.get("/v1/parametroOb/{id}")  # Endpoint de inicio, todos los endpoints se acompañan de una función
async def consultaUno(id:int):
    return {"Se encontró el usuario": id}  # Formato JSON

@router.get("/v1/parametroOp/")  # Endpoint de inicio, todos los endpoints se acompañan de una función
async def consultaTodos(id:Optional[int]=None):
    if id is not None:
        for usuario in usuarios:
            if usuario["id"] == id:
                return{"Mensaje": "Usuario encontrado", "Usuario": usuario}
        return{"Mensaje": "Usuario no encontrado", "Usuario": id}
    else:
        return{"Mensaje": "No se proporcionó ID"}
    


