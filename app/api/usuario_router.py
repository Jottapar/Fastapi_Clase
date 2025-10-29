from fastapi import APIRouter, HTTPException, Depends
from app.services import usuario_services
from sqlalchemy.orm import Session
from app.schemas.usuario_schema import UsuarioCreate, UsuarioResponse, UsuarioUpdate, UsuarioPut
from app.db.database import get_db

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)

@router.get("/", response_model=list[UsuarioResponse])
def list_usuarios(db: Session = Depends(get_db)):
    try:
        return usuario_services.get_all_usuarios(db)
    except HTTPException as e:
        raise e

@router.get("/{usuario_id}", response_model=UsuarioResponse)
def get_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = usuario_services.get_usuario_by_id(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.post("/", response_model=UsuarioResponse)
def create_usuario(usuario: UsuarioCreate , db: Session = Depends(get_db)):
    try:
        usuario = usuario_services.create_usuario(db, usuario)
        return usuario
    except HTTPException as e:
        raise e

@router.patch("/{usuario_id}", response_model=UsuarioResponse)
def patch_usuario(usuario_id: int, body: UsuarioUpdate, db: Session = Depends(get_db)):
    try:
        usuario = usuario_services.parcial_update_usuario(db, usuario_id, body)
        return usuario
    except HTTPException as e:
        raise e

@router.put("/{usuario_id}", response_model=UsuarioResponse)
def put_usuario(usuario_id: int, body: UsuarioPut, db: Session = Depends(get_db)):
    return usuario_services.update_usuario(db, usuario_id, body)