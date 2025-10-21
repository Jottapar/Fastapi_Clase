from pydantic import BaseModel
from datetime import date, datetime

class OrdenTrabajoCreate(BaseModel):
    fecha_creacion: date
    detalles: str | None = None
    direccion: str
    fecha_ope: datetime
    estado: str | None = None
    acta_id: int | None = None
    usuario_id: int | None = None


class OrdenTrabajoResponse(BaseModel):
    id: int
    fecha_creacion: date
    detalles: str | None = None
    direccion: str
    fecha_ope: datetime
    estado: str | None = None
    acta_id: int | None = None
    usuario_id: int | None = None

    class Config:
        orm_mode = True
