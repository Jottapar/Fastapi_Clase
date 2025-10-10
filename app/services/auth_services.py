from datetime import datetime, timedelta
from fastapi import HTTPException
from app.models import Usuario
from passlib.context import CryptContext
from sqlalchemy.orm import Session
import jwt  

pwcontext = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_contrasena(contrasena: str, contrasena_hash: str):
    return pwcontext.verify(contrasena, contrasena_hash)

def autenticar_usuario(db: Session, correo: str, contrasena: str):
    usuario = db.query(Usuario).filter(Usuario.correo == correo).first()
    if not usuario:
        return HTTPException(status_code=400, detail="Usuario no encontrado")
    if not verificar_contrasena(contrasena, usuario.contrasena):
        return HTTPException(status_code=400, detail="Correo o contraseña incorrectos")
    if usuario.estado != "Activo":
        return HTTPException(status_code=400, detail="Usuario inactivo")
    return usuario

def crear_token_usuario(data: dict):
    # Aquí iría la lógica para crear un token JWT
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=60)
    #actualizar el diccionario con la fecha de expiracion
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, "secret", algorithm="HS256")
    return token