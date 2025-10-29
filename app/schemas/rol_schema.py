from pydantic import BaseModel, EmailStr

#schema para el login
class RolSchemaResponse(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True
