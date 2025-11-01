from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session

from app.schemas.tarea_schema import TareaSchemaResponse, TareaSchemaCreate
from app.db.database import get_db
from app.services import tarea_services

router = APIRouter(
    prefix="/tarea",
    tags=["tarea"]
)

@router.post("/", response_model=TareaSchemaResponse)
def create_tarea(tarea_entry:TareaSchemaCreate, db: Session = Depends(get_db)):
    try:
        tarea = tarea_services.create_tarea(db,tarea_entry)
        return tarea
    except HTTPException as e:
        raise e
    
    