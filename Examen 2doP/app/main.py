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

tickets = []                
contador_tickets = 1   

class ticketCreate(BaseModel):
    nombre: str = Field(..., min_length=5, max_length=50, example="Estrella Marco")
    descripción: str= Field(...,gt=0, description="Se trabo")
    Prioridad: str= Field(...,gt=0, description="baja,media o alta")
class ticket(ticketCreate):
    id: int
    estado: str = "disponible"

@app.get("/v1/parametroOp/",tags=["Parametro Opcional"])  # Endpoint de inicio, todos los endpoints se acompañan de una función
async def consultaTodos(id:Optional[int]=None):
    if id is not None:
        for ticket in tickets:
            if ticket["id"] == id:
                return{"Mensaje": "ticket encontrado", "ticket": ticket}
        return{"Mensaje": "ticket no encontrado", "ticket": id}
    else:
        return{"Mensaje": "No se proporcionó ID"}

@app.get("/v1/tickets/{id}",tags=["CRUD HTTP"])  # Endpoint de inicio, todos los endpoints se acompañan de una función
async def leer_tickets():
    return {
        "status":"200",
        "total": len(ticket)
        }  # Formato JSON

class Prestamo(PrestamoCreate):
    id: int
    fecha_prestamo: datetime
    fecha_devolucion: Optional[datetime] = None
    activo: bool = True


@app.get("/", tags=["Inicio"])
async def bienvenida():
    return {
        "mensaje": "¡Bienvenido a la Biblioteca Digital!",
        "endpoints": {
            "POST /libros": "Registrar un libro",
            "GET /libros": "Listar todos los libros disponibles",
            "GET /libros/buscar/{nombre}": "Buscar libro por nombre",
            "POST /prestamos": "Registrar préstamo",
            "PUT /prestamos/{id}/devolver": "Marcar libro como devuelto",
            "DELETE /prestamos/{id}": "Eliminar registro de préstamo"
        }
    }

# Registrar 
@app.post("/tickets", status_code=status.HTTP_201_CREATED, tags=["tickets"])
async def registrar_tickets(ticket: ticketCreate):
    global contador_tickets
    
    # Valida el nombre 
    if not tickets.nombre or len(tickets.nombre.strip()) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El nombre del tickets no es válido"
        )
    
    nuevo_ticket = Libro(
        id=contador_libros,
        **libro.dict()
    )
    libros.append(nuevo_libro)
    contador_libros += 1
    
    return {
        "status": "201",
        "mensaje": "Libro registrado exitosamente",
        "libro": nuevo_libro
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
@app.get("/tickets/buscar/{id}", tags=["tickets"])
async def buscar_por_id(id: int, userAuth: str = Depends(verificar_Peticion)):
    # Validar el id
    if not id or len(id.strip()) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El id de búsqueda no es válido"
        )
    
    resultados = []
    for ticket in tickets:
        if id.lower() in ticket.id.lower():
            resultados.append(ticket)
    
    return {
        "status": "200",
        "busqueda": id,
        "total": len(resultados),
        "ticket": resultados
    }

    raise HTTPException(
        status_code=400,
        detail="El id no existe"
    )
    

    
    # Actualizar estado
    ticket_encontrado.estado = "prestado"
    
    

@app.delete("/v1/tickets/{id}", tags=["CRUD HTTP"])  # Endpoint de inicio, todos los endpoints se acompañan de una función
async def eliminar_tickets(ticket: dict):
    for tck in tickets:
        if tck["id"] == ticket.get("id"):
            tickets.remove(ticket)
            return{
                "status":"200",
                "mensaje":"ticket eliminado",
                "Tickets":ticket
            }
    raise HTTPException(       
        status_code=400,
        detail="El id no existe, no se puede eliminar"
    )

# Endpoint para obtener específico
@app.get("/tickets/{id}", tags=["tickets"])
async def obtener_tickets(id: int):
    for ticket in tickets:
        if ticket.id == id:
            return {
                "status": "200",
                "ticket": ticket
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="ticket no encontrado"
    )