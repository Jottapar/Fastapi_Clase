from pydantic import BaseModel

class InsumoSchemaCreate(BaseModel):
    nombre: str
    tipo: str

class InsumoSchemaResponse(BaseModel):
    id: int
    nombre: str
    tipo: str

    class Config:
        orm_mode = True
