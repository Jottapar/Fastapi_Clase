from app.db.database import SessionLocal
from app.schemas.insumo_schema import InsumoSchemaCreate
from app.models.Insumo import Insumo

from fastapi import HTTPException
from sqlalchemy.orm import Session

def create_insumo(db: Session, insumo:InsumoSchemaCreate):

    existing_insumo = db.query(Insumo).filter((Insumo.nombre == insumo.nombre)).first()
    
    if existing_insumo:
        raise HTTPException(status_code=400, detail='Este insumo ya existe')
    
    db_insumo = Insumo(
        nombre = insumo.nombre,
        tipo = insumo.tipo
    )

    db.add(db_insumo)
    db.commit()
    db.refresh(db_insumo)
    return db_insumo



