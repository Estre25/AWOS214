#Endpoints usuarios
from fastapi import status,Depends, HTTPException, APIRouter
from app.models.usuario import usuario_create
from app.data.database import usuarios 
from app.security.auth import verificar_Peticion

from sqlalchemy.orm import Session
from app.data.db import get_db
from app.data.usuario import Usuario as usuarioDB

router = APIRouter(
    prefix = "/v1/usuarios", tags=["CRUD HTTP"]
)

@router.get("/")  # Endpoint de inicio, todos los endpoints se acompañan de una función
async def leer_usuarios(db:Session= Depends(get_db)):
    queryUsers= db.query(usuarioDB).all()
    return {
        "status":"200",
        "total": len(queryUsers),
        "usuarios":queryUsers
        }  # Formato JSON

@router.post("/{id}")  # Endpoint de inicio, todos los endpoints se acompañan de una función
async def crear_usuario(usuarioP:usuraio_create,db:Session= Depends(get_db)):

    nuevoUsuario= usuarioDB(nombre= usuarioP.nombre, edad= usuarioP.edad)
    db.add(nuevoUsuario)
    db.commit()
    db.refresh(nuevoUsuario)
    
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
