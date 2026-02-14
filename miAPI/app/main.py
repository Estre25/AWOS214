from fastapi import FastAPI, status, HTTPException
import asyncio
from typing import Optional

#Instancia del servidor
app = FastAPI(
    title="Mi primer API",
    description="Estrella",
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

@app.get("/v1/parametroOb/{id}",tags=["Parametro Obligatorio"])  # Endpoint de inicio, todos los endpoints se acompañan de una función
async def consultaUno(id:int):
    return {"Se encontró el usuario": id}  # Formato JSON

# Endpoint de inicio, todos los endpoints se acompañan de una función
@app.get("/v1/parametroOp/", tags=["Parametro Opcional"])
async def consultaTodos(id: Optional[int] = None):
    if id is not None:
        for usuario in usuarios:
            if usuario["id"] == id:
                return {"Mensaje": "Usuario encontrado", "Usuario": usuario}
        # Si terminó el bucle sin encontrar
        return {"Mensaje": "Usuario no encontrado", "ID buscado": id}
    else:
        return {"Mensaje": "No se proporcionó ID"}

@app.get("/v1/usuarios/", tags=["CRUD HTTP"])
async def leer_usuarios( ):
    return{
        "status":"200",
        "total": len(usuarios),
        "usuarios": usuarios
    }

@app.post("/v1/usuarios/", tags=["CRUD HTTP"], status_code=status.HTTP_201_CREATED)
async def crear_usuarios(usuario:dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(
                status_code=400,
                detail="El id ya existe"
            )
    usuarios.append(usuario)
    return{
        "mensaje":"Usuario Agregado",
        "Usuario":usuario
    }   

@app.put("/v1/usuarios/", tags=["CRUD HTTP"], status_code=status.HTTP_200_OK)
async def actualizar_usuarios(usuario:dict):
    for i, usr in enumerate (usuarios):
        if usr["id"] == usuario.get("id"):
            usuarios[i] = usuario
            return{
                 "mensaje":"Usuario Actualizado",
                 "Usuario":usuario
                 } 
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
        )        

@app.delete("/v1/usuarios/", tags=["CRUD HTTP"], status_code=status.HTTP_200_OK)
async def eliminar_usuarios(usuario:dict):
    for i,usr in enumerate(usuarios):
        if usr["id"] == usuario.get("id"):
            usuario_eliminado = usuarios.pop(i)
            return{
                "mensaje":"Usuario Eliminado",
                "usuario": usuario_eliminado
            }
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )        