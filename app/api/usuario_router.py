from fastapi import APIRouter, HTTPException, Depends
from app.services import usuario_services
from sqlalchemy.orm import Session
from app.schemas.usuario_schema import UsuarioCreate, UsuarioResponse
from app.db.database import get_db

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)

@router.get("/", response_model=list[UsuarioResponse])
def list_usuarios(db: Session = Depends(get_db)):
    return usuario_services.get_all_usuarios(db)

@router.get("/{usuario_id}", response_model=UsuarioResponse)
def get_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = usuario_services.get_usuario_by_id(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.post("/", response_model=UsuarioResponse)
def create_usuario(usuario: UsuarioCreate , db: Session = Depends(get_db)):
    return usuario_services.create_usuario(db, usuario)