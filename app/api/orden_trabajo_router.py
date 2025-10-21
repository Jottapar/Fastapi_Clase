from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.orden_trabajo_schema import OrdenTrabajoCreate, OrdenTrabajoResponse
from app.services import orden_trabajo_services
from app.db.database import get_db

router = APIRouter(
    prefix="/orden_de_trabajo",
    tags=["ordenes_de_trabajo"]
)

@router.get("/", response_model=list[OrdenTrabajoResponse])
def list_ordenes(db: Session = Depends(get_db)):
    try:
        return orden_trabajo_services.get_all_ordenes(db)
    except HTTPException as e:
        raise e


@router.get("/{orden_id}", response_model=OrdenTrabajoResponse)
def get_orden(orden_id: int, db: Session = Depends(get_db)):
    orden = orden_trabajo_services.get_orden_by_id(db, orden_id)
    if not orden:
        raise HTTPException(status_code=404, detail="Orden de trabajo no encontrada")
    return orden


@router.post("/", response_model=OrdenTrabajoResponse)
def create_orden(orden: OrdenTrabajoCreate, db: Session = Depends(get_db)):
    try:
        nueva_orden = orden_trabajo_services.create_orden(db, orden)
        return nueva_orden
    except HTTPException as e:
        raise e
