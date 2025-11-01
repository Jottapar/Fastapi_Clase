from app.db.database import SessionLocal
from app.schemas.tarea_schema import TareaSchemaCreate
from app.models.Tarea import Tarea

from fastapi import HTTPException
from sqlalchemy.orm import Session

def create_tarea(db: Session, tarea:TareaSchemaCreate):

    existing_tarea = db.query(Tarea).filter((Tarea.tarea == tarea.tarea)).first()
    
    if existing_tarea:
        raise HTTPException(status_code=400, detail='Este tarea ya existe')
    
    db_tarea = Tarea(
        tarea = tarea.tarea,
        estado = 'pendiente'
    )

    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea



