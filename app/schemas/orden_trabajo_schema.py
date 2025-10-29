from pydantic import BaseModel
from datetime import date, datetime

from app.schemas.acta_schema import ActaResponse
from app.schemas.usuario_schema import UsuarioResponse

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
    #traer el usuario y el acta relacionados
    usuario: UsuarioResponse | None = None
    acta: ActaResponse | None = None

    class Config:
        orm_mode = True

class PaginatedOrdenTrabajoResponse(BaseModel):
    total: int
    skip: int
    limit: int
    items: list[OrdenTrabajoResponse]