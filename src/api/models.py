# SQLAlchemy ORM Models
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from api.database import Base

class TelegramMessage(Base):
    __tablename__ = "telegram_messages"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    date = Column(DateTime)
    has_media = Column(Boolean)
    channel = Column(String)
