from fastapi import HTTPException
from app.models.Usuario import Usuario
from app.models.Rol import Rol                     

from app.db.database import SessionLocal
from sqlalchemy.orm import Session

from app.schemas.usuario_schema import UsuarioCreate, UsuarioUpdate, UsuarioPut
from passlib.context import CryptContext

#configuramos el encriptador de contraseñas
pwcontext = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_contrasena(contrasena: str):
    return pwcontext.hash(contrasena)

#equivante a una consulta select * from usuarios
def get_all_usuarios(db: Session):
    usuarios = db.query(Usuario).all()    
    return usuarios

#equivante a una consulta select * from usuarios where id= usuario_id
def get_usuario_by_id(db: Session, usuario_id: int):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    return usuario

#equivante a un insert into usuarios (nombre, email, is_active, password) values (...)
def create_usuario(db: Session, usuario: UsuarioCreate):

    #validar si el correo o dcuemnto ya existe
    existing_usuario = db.query(Usuario).filter((Usuario.correo == usuario.correo) | (Usuario.doc_identidad == usuario.doc_identidad)).first()

    if existing_usuario: 
        raise HTTPException(status_code=400, detail="El correo o documento ya está en uso") 
    
    #validar si el rol existe
    rol = db.query(Rol).filter(Rol.id == usuario.rol_id).first()

    if not rol:
        raise HTTPException(status_code=400, detail="El rol no existe")

    db_usuario = Usuario(
        nombre_completo = usuario.nombre_completo,
        doc_identidad = usuario.doc_identidad,
        celular = usuario.celular,
        correo = usuario.correo,
        estado = "Activo",
        rol_id = usuario.rol_id,
        contrasena = hash_contrasena(usuario.contrasena) 
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def actualizar_usuario_parcial(db: Session, usuario_id: int, body: UsuarioUpdate) -> Usuario:
    usuario = db.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    data = body.dict(exclude_unset=True)

    for k, v in data.items():
        setattr(usuario, k, v)

    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

def reemplazar_usuario_total(db: Session, usuario_id: int, body: UsuarioPut) -> Usuario:
    usuario = db.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    data = body.dict()

    usuario.doc_identidad = data["doc_identidad"]
    usuario.nombre_completo = data["nombre_completo"]
    usuario.celular = data.get("celular")
    usuario.correo = data.get("correo")

    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario