from sqlalchemy.orm import Session
from . import models
from datetime import date
from typing import List, Optional

def create_patent(db: Session, patent_data: dict) -> models.Patent:
    db_patent = models.Patent(**patent_data)
    db.add(db_patent)
    db.commit()
    db.refresh(db_patent)
    return db_patent

def get_patent(db: Session, patent_id: int) -> Optional[models.Patent]:
    return db.query(models.Patent).filter(models.Patent.id == patent_id).first()

def get_patents(db: Session, skip: int = 0, limit: int = 100) -> List[models.Patent]:
    return db.query(models.Patent).offset(skip).limit(limit).all()

def update_patent(db: Session, patent_id: int, update_data: dict) -> Optional[models.Patent]:
    db_patent = db.query(models.Patent).filter(models.Patent.id == patent_id).first()
    if db_patent:
        for key, value in update_data.items():
            setattr(db_patent, key, value)
        db.commit()
        db.refresh(db_patent)
    return db_patent

def delete_patent(db: Session, patent_id: int) -> Optional[models.Patent]:
    db_patent = db.query(models.Patent).filter(models.Patent.id == patent_id).first()
    if db_patent:
        db.delete(db_patent)
        db.commit()
    return db_patent
