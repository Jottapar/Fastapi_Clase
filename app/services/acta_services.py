from fastapi import HTTPException
from app.models.Acta import Acta
from app.models.Rol import Rol                     

from app.db.database import SessionLocal
from sqlalchemy.orm import Session

from app.schemas.acta_schema import ActaCreate
from passlib.context import CryptContext

#equivante a una consulta select * from actas
def get_all_actas(db: Session):
    actas = db.query(Acta).all()    
    return actas

#equivante a una consulta select * from actas where id= acta_id
def get_acta_by_id(db: Session, acta_id: int):
    acta = db.query(Acta).filter(Acta.id == acta_id).first()
    return acta

#equivante a un insert into acta (numero, observacion) values (...)
def create_acta(db: Session, acta: ActaCreate):

    #validar si el correo o dcuemnto ya existe
    existing_acta = db.query(Acta).filter((Acta.numero == acta.numero)).first()

    if existing_acta: 
        raise HTTPException(status_code=400, detail="El numero de acta ya está en uso") 
    
    db_acta = Acta(
        numero = acta.numero,
        observaciones = acta.observaciones
    )

    db.add(db_acta)
    db.commit()
    db.refresh(db_acta)
    return db_acta