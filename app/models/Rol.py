from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db import database
from app.db.database import Base

class Rol(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)

    usuarios = relationship("Usuario", back_populates="rol")
