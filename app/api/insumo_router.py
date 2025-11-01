from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session

from app.schemas.insumo_schema import InsumoSchemaResponse, InsumoSchemaCreate
from app.db.database import get_db
from app.services import insumo_services

router = APIRouter(
    prefix="/insumo",
    tags=["insumo"]
)

@router.post("/", response_model=InsumoSchemaResponse)
def create_insumo(insumo_entry:InsumoSchemaCreate, db: Session = Depends(get_db)):
    try:
        insumo = insumo_services.create_insumo(db,insumo_entry)
        return insumo
    except HTTPException as e:
        raise e
    
    