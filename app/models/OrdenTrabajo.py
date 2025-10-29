from sqlalchemy import Column, Integer, String, Text, Date, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class OrdenTrabajo(Base):
    __tablename__ = 'ordenes_trabajo'

    #atributos de la tabla
    id = Column(Integer, primary_key=True, index=True)
    fecha_creacion = Column(Date, nullable=False)
    detalles = Column(Text, nullable=True)
    direccion = Column(String(100), nullable=False)
    fecha_ope = Column(DateTime, nullable=False)
    estado = Column(String(20), nullable=True)

    #atributos de historial
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, nullable = True)

    #Foreign Keys
    acta_id = Column(Integer, ForeignKey('acta.id',onupdate="CASCADE" ,ondelete="SET NULL"))
    usuario_id = Column(Integer, ForeignKey('usuarios.id', onupdate="CASCADE", ondelete="SET NULL"))

    #realciones con las tablas
    usuario = relationship('Usuario', back_populates='ordenes_trabajo')
    acta = relationship('Acta', back_populates='ordenes_trabajo')
    asignaciones_ordenes_trabajo = relationship('AsignacionOrdenTrabajo', back_populates= 'ordenes_trabajo')