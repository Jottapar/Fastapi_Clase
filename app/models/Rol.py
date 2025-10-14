from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.db import database
from app.db.database import Base

class Rol(Base):
    __tablename__ = "roles"

    #atributos de la tabla
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)

    #atributos de historial
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, nullable = True)

    #relacion con tabla
    usuarios = relationship("Usuario", back_populates="rol")
