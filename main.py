# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine, get_db

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post("/detections/", response_model=schemas.ObjectDetection)
def create_detection(detection: schemas.ObjectDetectionCreate, db: Session = Depends(get_db)):
    return crud.create_object_detection(db=db, detection=detection)

@app.get("/detections/", response_model=list[schemas.ObjectDetection])
def read_detections(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    detections = crud.get_object_detections(db, skip=skip, limit=limit)
    return detections

@app.get("/detections/{detection_id}", response_model=schemas.ObjectDetection)
def read_detection(detection_id: int, db: Session = Depends(get_db)):
    detection = crud.get_object_detection(db, detection_id=detection_id)
    if detection is None:
        raise HTTPException(status_code=404, detail="Detection not found")
    return detection
