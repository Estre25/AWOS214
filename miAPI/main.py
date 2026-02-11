from fastapi import FastAPI  
import asyncio
from typing import Optional

#Instancia del servidor
app = FastAPI(
    title="Mi primer API",
    description="Carlos",
    version="1.0.0"
    )

usuarios = [
    {"id": 1, "nombre": "Juan", "edad": 21},
    {"id": 2, "nombre": "Israel", "edad": 21},
    {"id": 3, "nombre": "Sofi", "edad": 21}
]

@app.get("/",tags=["Inicio"])  # Endpoint de inicio, todos los endpoints se acompañan de una función
async def bienvenida():
    return {"mensaje": "¡Bienvenido a mi API!"}  # Formato JSON

@app.get("/HolaMundo",tags=["Bienvenida asincrona"])  # Endpoint
async def hola():
    await asyncio.sleep(7)#Simulacion de uns 
    return {"mensaje": "¡Hola Mundo FastAPI!",
            "estatus":"200"
            }  # Formato JSON

@app.get("/v1/usuario/{id}",tags=["Parametro Obligatorio"])  # Endpoint de inicio, todos los endpoints se acompañan de una función
async def consultaUno(id:int):
    return {"Se encontró el usuario": id}  # Formato JSON

# Endpoint de inicio, todos los endpoints se acompañan de una función
@app.get("/v1/usuario/", tags=["Parametro Opcional"])
async def consultaTodos(id: Optional[int] = None):
    if id is not None:
        for usuario in usuarios:
            if usuario["id"] == id:
                return {"Mensaje": "Usuario encontrado", "Usuario": usuario}
        # Si terminó el bucle sin encontrar
        return {"Mensaje": "Usuario no encontrado", "ID buscado": id}
    else:
        return {"Mensaje": "No se proporcionó ID"}