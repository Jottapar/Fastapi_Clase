from sqlalchemy import create_engine, MetaData
from app.core.config import settings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#motor de conexion
engine = create_engine(settings.DATABASE_URL)
meta = MetaData()

#sesion de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#modelo base
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()