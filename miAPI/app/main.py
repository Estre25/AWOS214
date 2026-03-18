from fastapi import FastAPI 
from app.routers import usuarios, varios

#Instancia del servidor
app = FastAPI(
    title="Mi primer API",
    description="Estrella",
    version="1.0.0"
    )

# Se registran todos los endpoints del router
app.include_router(usuarios.router)
app.include_router(varios.router)


