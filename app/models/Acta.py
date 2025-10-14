from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.db.database import Base

class Acta(Base):
    __tablename__ = 'acta'

    #atributos de la tabla
    id = Column(Integer, Primary_key=True, Index=True)
    numero = Column(String(7), nullable=False)
    observaciones = Column(Text, nullable=True)

    ##atributos de historial
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, nullable=True)

    #relacion con tabla
    ordenes_trabajo = relationship('Ordenes_Trabajo', back_populates='acta')
