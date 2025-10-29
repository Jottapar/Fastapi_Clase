from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.OrdenTrabajo import OrdenTrabajo
from app.models.Acta import Acta
from app.models.Usuario import Usuario
from app.schemas.orden_trabajo_schema import OrdenTrabajoCreate

def get_all_ordenes(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        estado: str | None = None,
        usuario_id: int | None = None,
        acta_id: int | None = None
    ):

    if estado or usuario_id or acta_id:
        query = db.query(OrdenTrabajo)
        if estado:
            query = query.filter(OrdenTrabajo.estado == estado)
        if usuario_id:
            query = query.filter(OrdenTrabajo.usuario_id == usuario_id)
        if acta_id:
            query = query.filter(OrdenTrabajo.acta_id == acta_id)
        ordenes = query.offset(skip).limit(limit).all()
        return ordenes
    
    total = db.query(OrdenTrabajo).count()
    ordenes = db.query(OrdenTrabajo).offset(skip).limit(limit).all()

    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "items": ordenes
    }


def get_orden_by_id(db: Session, orden_id: int):
    orden = db.query(OrdenTrabajo).filter(OrdenTrabajo.id == orden_id).first()
    return orden


def create_orden(db: Session, orden: OrdenTrabajoCreate):

    #validar si la orden ya existe
    existing_orden = db.query(OrdenTrabajo).filter((OrdenTrabajo.detalles == orden.detalles) & (OrdenTrabajo.fecha_creacion == orden.fecha_creacion)).first()
    if existing_orden:
        raise HTTPException(status_code=400, detail="La orden de trabajo ya existe")
    
    #validar si el usuario existe
    usuario = db.query(Usuario).filter(Usuario.id == orden.usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=400, detail="El usuario no existe")
    
    #validar si el acta existe
    acta = db.query(Acta).filter(Acta.id == orden.acta_id).first()
    if not acta:
        raise HTTPException(status_code=400, detail="El acta no existe")

    db_orden = OrdenTrabajo(
        fecha_creacion=orden.fecha_creacion,
        detalles=orden.detalles,
        direccion=orden.direccion,
        fecha_ope=orden.fecha_ope,
        estado=orden.estado,
        acta_id=orden.acta_id,
        usuario_id=orden.usuario_id
    )

    db.add(db_orden)
    db.commit()
    db.refresh(db_orden)
    return db_orden
