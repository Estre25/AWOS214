#Endpoints usuarios
from fastapi import status,Depends, HTTPException, APIRouter
from app.models.usuario import usuario_create
from app.data.database import usuarios
from app.security.auth import verificar_Peticion

router = APIRouter(
    prefix = "/v1/usuarios", tags=["CRUD HTTP"]
)

@router.get("/")  # Endpoint de inicio, todos los endpoints se acompañan de una función
async def leer_usuarios():
    return {
        "status":"200",
        "total": len(usuarios),
        "usuarios":usuarios
        }  # Formato JSON

@router.post("/{id}")  # Endpoint de inicio, todos los endpoints se acompañan de una función
async def crear_usuario(usuario:usuario_create):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(
                status_code=400,
                detail="El id ya existe"
            )
    usuarios.append(usuario)
    return{
        "mensaje":"Usuario agregado",
        "Usuario":usuario
    }

@router.put("/{id}")  # Endpoint de inicio, todos los endpoints se acompañan de una función
async def actualizar_usuario(usuario: dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            usuarios.append(usuario)
            return{
                "status":"200",
                "mensaje":"Usuario actualizado",
                "Usuario":usuario
            }
    raise HTTPException(
        status_code=400,
        detail="El id no existe, no se puede actualizar"
    )

@router.delete("/{id}")
async def eliminar_usuario(id: int, userAuth: str = Depends(verificar_Peticion)):
    # Buscar el usuario por id
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)
            return {
                "status": "200",
                "mensaje": f"Usuario eliminado por {userAuth}",
                "usuario_eliminado": usuario
            }
    
    # Si no encuentra el id
    raise HTTPException(
        status_code=400,
        detail="El id no existe, no se puede eliminar"
    )
