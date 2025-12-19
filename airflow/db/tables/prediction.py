from ..database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from sqlalchemy.sql import func

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True)

    label = Column(String(10))
    text = Column(Text)
    airline = Column(String(50))
    airline_sentiment_confidence = Column(Float)
    negativereason = Column(String(50))
    tweet_created = Column(DateTime(timezone=True))
    
    predicted_at = Column(DateTime(timezone=True), server_default=func.now())