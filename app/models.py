from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500))
    description = Column(String(500))
    url = Column(String(1000))
    published_at = Column(DateTime, default=datetime.utcnow)
    
    