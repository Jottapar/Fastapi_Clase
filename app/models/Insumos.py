from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlachemy.orm import relationship
from app.db.database import Base

class Insumos(Base):
    __tablename__ = 'insumos'

    #atributos de la tabla
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20), nullable=False)
    tipo = Column(String(20), nullable=True)
    
    #atributos de historial
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, nullable= True)

    #relacion con tabla
    asignaciones_ordenes_trabajo = relationship('Asignaciones_Ordenes_Trabajo', back_populates='insumos')

