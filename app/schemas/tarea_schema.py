from pydantic import BaseModel

class TareaSchemaCreate(BaseModel):
    tarea: str

class TareaSchemaResponse(BaseModel):
    id: int
    tarea: str
    estado: str

    class Config:
        orm_mode = True
