from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.db.database import Base

class TareaOperacion(Base):
    __tablename__ = 'tareas_ope'

    #atributos de la tabla
    id = Column(Integer, primary_key=True, index=True)
    tarea = Column(Text, nullable=False)
    estado = Column(String(20), nullable=True)

    #atributos de historial
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, nullable= True)

    #relacion con tabla
    asignaciones_ordenes_trabajo = relationship('AsignacionOrdenTrabajo', back_populates='tareas_ope')