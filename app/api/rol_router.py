from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session

from app.schemas.rol_schema import RolSchemaResponse
from app.db.database import get_db
from app.services import rol_services

router = APIRouter(
    prefix="/rol",
    tags=["rol"]
)

@router.post("/", response_model=RolSchemaResponse)
def create_rol(usuario:RolSchemaResponse, db: Session = Depends(get_db)):
    try:
        rol = rol_services.create_rol(db,usuario)
        return rol
    except HTTPException as e:
        raise e
    
    