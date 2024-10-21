# crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def create_object_detection(db: Session, detection: schemas.ObjectDetectionCreate):
    db_detection = models.ObjectDetection(**detection.dict())
    db.add(db_detection)
    db.commit()
    db.refresh(db_detection)
    return db_detection

def get_object_detections(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ObjectDetection).offset(skip).limit(limit).all()

def get_object_detection(db: Session, detection_id: int):
    return db.query(models.ObjectDetection).filter(models.ObjectDetection.id == detection_id).first()
