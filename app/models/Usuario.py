from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db import database
from app.db.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String(100), nullable=False)
    doc_identidad = Column(String(10), nullable=False)
    celular = Column(String(13))
    correo = Column(String(50), unique=True, nullable=False)
    contrasena = Column(String, nullable=False)
    estado = Column(String(10), nullable=False)
    rol_id = Column(Integer, ForeignKey("roles.id", ondelete="SET NULL"))

    rol = relationship("Roles", back_populates="usuarios")

