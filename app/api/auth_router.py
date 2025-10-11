

from fastapi import APIRouter, Depends
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.schemas.usuario_schema import UsuarioLogin
from app.services import auth_services

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login")
def login(request: UsuarioLogin, db: Session = Depends(get_db)):
    usuario = auth_services.autenticar_usuario(db, request.correo, request.contrasena)
    access_token = auth_services.crear_token_usuario(data={"sub": usuario.correo})

    return {
        "access_token": access_token, 
        "token_type": "bearer",
        "usuario": {
            "id": usuario.id,
            "nombre_completo": usuario.nombre_completo,
            "correo": usuario.correo,
            "rol_id": usuario.rol_id
        }
    }