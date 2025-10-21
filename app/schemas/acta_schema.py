from pydantic import BaseModel

#schema para todo
class ActaCreate(BaseModel):
    numero: str
    observaciones: str

class ActaResponse(BaseModel):
    id: int
    numero: str
    observaciones: str

    class Config:
        orm_mode = True

