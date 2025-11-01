from app.db.database import SessionLocal
from app.schemas.usuario_schema import RolSchemaResponse
from app.models.Rol import Rol

from fastapi import HTTPException

from sqlalchemy.orm import Session



def create_rol(db: Session, usuario:RolSchemaResponse):

    existing_usuario = db.query(Rol).filter((Rol.nombre == usuario.nombre)).first()
    
    if existing_usuario:
        raise HTTPException(status_code=400, detail='Este rol ya existe')
    
    db_rol = Rol(
        nombre_rol = usuario.nombre
    )

    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol



