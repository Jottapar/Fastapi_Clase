from app.db.database import SessionLocal
from app.schemas.rol_schema import RolSchemaCreate
from app.models.Rol import Rol

from fastapi import HTTPException
from sqlalchemy.orm import Session

def create_rol(db: Session, rol:RolSchemaCreate):

    existing_rol = db.query(Rol).filter((Rol.nombre == rol.nombre)).first()
    
    if existing_rol:
        raise HTTPException(status_code=400, detail='Este rol ya existe')
    
    db_rol = Rol(
        nombre = rol.nombre
    )

    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol
