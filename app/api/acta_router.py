from fastapi import APIRouter, HTTPException, Depends
from app.services import acta_services
from sqlalchemy.orm import Session
from app.schemas.acta_schema import ActaCreate, ActaResponse
from app.db.database import get_db

router = APIRouter(
    prefix="/acta",
    tags=["acta"]
)

@router.get("/", response_model=list[ActaResponse])
def list_actas(db: Session = Depends(get_db)):
    try:
        return acta_services.get_all_actas(db)
    except HTTPException as e:
        raise e

@router.get("/{acta_id}", response_model=ActaResponse)
def get_acta(acta_id: int, db: Session = Depends(get_db)):
    acta = acta_services.get_acta_by_id(db, acta_id)
    if not acta:
        raise HTTPException(status_code=404, detail="Acta no encontrada")
    return acta

@router.post("/", response_model=ActaResponse)
def create_acta(acta: ActaCreate , db: Session = Depends(get_db)):
    try:
        acta = acta_services.create_acta(db, acta)
        return acta
    except HTTPException as e:
        raise e
