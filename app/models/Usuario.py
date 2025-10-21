from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db import database
from app.db.database import Base
from app.models.Rol import Rol

class Usuario(Base):
    __tablename__ = "usuarios"

    #atributos de la tabla
    id = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String(100), nullable=False)
    doc_identidad = Column(String(10), nullable=False)
    celular = Column(String(13))
    correo = Column(String(50), unique=True, nullable=False)
    contrasena = Column(String, nullable=False)
    estado = Column(String(10), nullable=False)

    #foreign keys
    rol_id = Column(Integer, ForeignKey("roles.id", ondelete="SET NULL"))

    #relaciones con tablas
    rol = relationship("Rol", back_populates="usuarios")
    ordenes_trabajo = relationship('OrdenTrabajo', back_populates='usuarios')
    asignador_ordenes_trabajo = relationship(
        'AsignacionOrdenTrabajo', 
        foreign_keys='AsignacionOrdenTrabajo.asignador_id',
        back_populates='usuario_asignador')
    asignado_ordenes_trabajo = relationship(
        'AsignacionOrdenTrabajo', 
        foreign_keys='AsignacionOrdenTrabajo.asignado_id',
        back_populates='usuario_asignado')

