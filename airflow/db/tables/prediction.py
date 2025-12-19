from ..database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True)

    label = Column(String(50))
    text = Column(String(200))
    predicted_at = Column(DateTime(timezone=True), server_default=func.now())