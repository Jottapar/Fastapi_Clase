from pydantic import BaseModel, EmailStr

#schema para el login
class UsuarioLogin(BaseModel):
    correo: EmailStr
    contrasena: str

#schema para la lectura
class UsuarioBase(BaseModel):
    nombre_completo: str
    correo: str
    estado: str

#schema para la creacion
class UsuarioCreate(UsuarioBase):
    contrasena: str
    doc_identidad: str
    celular: str | None = None
    rol_id: int


#schema para la edicion parcial
class UsuarioUpdate (BaseModel):
    doc_identidad: str | None = None
    nombre_completo: str | None = None
    celular: str | None = None
    correo: EmailStr | None = None

#schema para la edicion parcial
class UsuarioPut (BaseModel):
    doc_identidad: str
    nombre_completo: str
    celular: str | None = None
    correo: EmailStr | None = None


#schema para la respuesta
class UsuarioResponse(UsuarioBase):
    id: int
    rol_id: int
    class Config:
        orm_mode = True

