from fastapi import FastAPI, status ,HTTPException 
from fastapi import FastAPI, status ,HTTPException, Depends 
import asyncio
from typing import Optional
from pydantic import BaseModel, Field
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

app = FastAPI(
    title="Tickets API",
    description="API para gestionar tickets",
    version="1.0.0"
)

security= HTTPBasic()
def verificar_Peticion(credenciales: HTTPBasicCredentials = Depends(security)):
    userAuth = secrets.compare_digest(credenciales.username, "soporte")
    passAuth = secrets.compare_digest(credenciales.password, "4321")
    
    if not (userAuth and passAuth):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales no Autorizadas"
        )
    return credenciales.username

libros = []          
prestamos = []       
contador_libros = 1  
contador_prestamos = 1  

class Usuario(BaseModel):
    nombre: str = Field(..., min_length=5, max_length=50, example="Estrella Marco")
    descripción: str= Field(...,gt=0, description="Se trabo")
    Prioridad: str= Field(...,gt=0, description="baja,media o alta")
    Estado: str= Field(...,gt=0, default="pendiente")
   

@app.get("/v1/tickets/{id}",tags=["CRUD HTTP"])  # Endpoint de inicio, todos los endpoints se acompañan de una función
async def leer_tickets():
    return {
        "status":"200",
        "total": len(ticket)
        }  # Formato JSON

@app.post("/v1/tickets/{id}",tags=["CRUD HTTP"])  # Endpoint de inicio, todos los endpoints se acompañan de una función
async def crear_tickets(ticket:ticket_create):
    for tck in ticket:
        if tck["id"] == ticket.id:
            raise HTTPException(
                status_code=400,
                detail="El id ya existe"
            )
    tickets.append(ticket)
    return{
        "mensaje":"ticket creado",
        "ticket":ticket
    }   
@app.put("/v1/tickets/{id}", tags=["CRUD HTTP"])  # Endpoint de inicio, todos los endpoints se acompañan de una función
async def actualizar_tickets(ticket: dict):
    for tck in tickets:
        if tck["id"] == ticket.get("id"):
            tickets[i] = ticket
            tickets.append(Estado)
            return{
                "status":"200",
                "mensaje":"Usuario actualizado",
                "Usuario":usuario
            }
    raise HTTPException(   
        status_code=400,
        detail="El id no existe, no se puede actualizar"
    )

# Buscar 
@app.get("/libros/buscar/{id}", tags=["Libros"])
async def buscar_por_nombre(nombre: str):
    # Validar el nombre 
    if not id or len(id.strip()) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El nombre de búsqueda no es válido"
        )
    
    resultados = []
    for libro in libros:
        if nombre.lower() in libro.nombre.lower():
            resultados.append(libro)
    
    return {
        "status": "200",
        "busqueda": nombre,
        "total": len(resultados),
        "libros": resultados
    }

    
    # Actualizar estado
    libro_encontrado.estado = "prestado"
    
    # Crear préstamo
    nuevo_prestamo = Prestamo(
        id=contador_prestamos,
        **prestamo.dict(),
        fecha_prestamo=datetime.now()
    )
    prestamos.append(nuevo_prestamo)
    contador_prestamos += 1
    
    return {
        "status": "201",
        "mensaje": "Préstamo registrado exitosamente",
        "prestamo": nuevo_prestamo
    }


# Eliminar el registro de un préstamo
@app.delete("/prestamos/{id}", tags=["Préstamos"])
async def eliminar_prestamo(id: int):
    # Buscar el préstamo
    prestamo_encontrado = None
    for prestamo in prestamos:
        if prestamo.id == id:
            prestamo_encontrado = prestamo
            break
    
    # 404 si el préstamo no existe
    if not prestamo_encontrado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Préstamo no encontrado"
        )
    
    # 409 si el préstamo ya no existe
    if not prestamo_encontrado.activo:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El registro de préstamo ya no existe"
        )
    
    # Si está activo, devolver el libro
    if prestamo_encontrado.activo:
        for libro in libros:
            if libro.id == prestamo_encontrado.libro_id:
                libro.estado = "disponible"
                break
    
   @app.delete("/v1/usuarios/", tags=["CRUD HTTP"], status_code=status.HTTP_200_OK)
async def eliminar_usuarios(usuario:dict):
    for i,usr in enumerate(usuarios):
@app.delete("/v1/usuarios/{id}", tags=["CRUD HTTP"])  # Endpoint de inicio, todos los endpoints se acompañan de una función
async def eliminar_usuario(usuario: dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            usuario_eliminado = usuarios.pop(i)
            usuarios.remove(usuario)
            return{
                "mensaje":"Usuario Eliminado",
                "usuario": usuario_eliminado
                "status":"200",
                "mensaje":"Usuario eliminado",
                "Usuario":usuario
            }
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )        
        status_code=400,
        detail="El id no existe, no se puede eliminar"
    )

# Endpoint para obtener un libro específico
@app.get("/libros/{id}", tags=["Libros"])
async def obtener_libro(id: int):
    for libro in libros:
        if libro.id == id:
            return {
                "status": "200",
                "libro": libro
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Libro no encontrado"
    )