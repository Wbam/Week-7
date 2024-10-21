# models.py
from sqlalchemy import Column, Integer, String, Float
from .database import Base

class ObjectDetection(Base):
    __tablename__ = "object_detection"

    id = Column(Integer, primary_key=True, index=True)
    image_path = Column(String, index=True)
    class_label = Column(String)
    confidence = Column(Float)
    bbox_x1 = Column(Float)
    bbox_y1 = Column(Float)
    bbox_x2 = Column(Float)
    bbox_y2 = Column(Float)
