from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from app.schemas.orden_trabajo_schema import OrdenTrabajoCreate, OrdenTrabajoResponse, PaginatedOrdenTrabajoResponse
from app.services import orden_trabajo_services
from app.db.database import get_db

router = APIRouter(
    prefix="/orden_de_trabajo",
    tags=["ordenes_de_trabajo"]
)

@router.get("/", response_model=PaginatedOrdenTrabajoResponse)
def list_ordenes(
        db: Session = Depends(get_db),
        skip: int = Query(0, ge=0, description="Número de registros a omitir"),
        limit: int = Query(10, le=1000, description="Número máximo de registros a retornar"),
        estado: str | None = Query(None, description="Filtrar por estado de la orden"),
        usuario_id: int | None = Query(None, description="Filtrar por ID de usuario"),
        acta_id: int | None = Query(None, description="Filtrar por ID de acta")
    ):
    #agregando paginacion y filtros en el futuro
    try:
        return orden_trabajo_services.get_all_ordenes(
            db,
            skip=skip,
            limit=limit,
            estado=estado,
            usuario_id=usuario_id,
            acta_id=acta_id
        )
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
