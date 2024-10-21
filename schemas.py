# schemas.py
from pydantic import BaseModel

class ObjectDetectionBase(BaseModel):
    image_path: str
    class_label: str
    confidence: float
    bbox_x1: float
    bbox_y1: float
    bbox_x2: float
    bbox_y2: float

class ObjectDetectionCreate(ObjectDetectionBase):
    pass

class ObjectDetection(ObjectDetectionBase):
    id: int

    class Config:
        orm_mode = True
