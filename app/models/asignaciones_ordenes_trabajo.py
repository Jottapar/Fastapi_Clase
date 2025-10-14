from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.db.database import Base

class Asignaciones_Ordenes_Trabajo(Base):
    __tablename__ = 'asignaciones_ordenes_trabajo'

    #atributos de la tabla
    id = Column(Integer, primary_key=True, index=True)
    estado = Column(String(20), nullable=True)

    #atributos de historial
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, nullable = True)

    #foreign Keys
    asignador_id = Column(Integer, ForeignKey('Usuarios.id', onupdate='CASCADE', ondelete='SET NULL'))
    orden_trabajo_id = Column(Integer, ForeignKey('ordenes_trabajo.id',onupdate='CASCADE', ondelete='SET NULL'))
    tarea_id = Column(Integer, ForeignKey('tarea.id', onupdate='CASCADE', ondelete='SET NULL'))
    insumo_id = Column(Integer, ForeignKey('insumos.id', onupdate='CASCADE', ondelete='SET NULL'))
    asignado_id = Column(Integer, ForeignKey('usuarios.id', onupdate='CASCADE', ondelete='SET NULL'))

    #relaciones con tablas
    usuarios = relationship('Usuarios', back_populates='asignador_ordenes_trabajo')
    usuario_asignado = relationship('Usuarios', back_populates='asignado_ordenes_trabajo')
    tareas_ope = relationship('Tareas_Ope', back_populates='asignaciones_ordenes_trabajo')
    insumos = relationship('Insumos', back_populates='asignaciones_ordenes_trabajo')
    ordenes_trabajo = relationship('Ordenes_Trabajo', back_populates= 'asignaciones_ordenes_trabajo')