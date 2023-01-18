from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID

from src.db.base import Base


class TimeBasedPrice(Base):

    price = Column(Float, nullable=False)
    item_id = Column(UUID, ForeignKey("item.id"))
    start_hour = Column(Integer, nullable=False)
    end_hour = Column(Integer, nullable=False)
    start_minutes = Column(Integer, nullable=False)
    end_minutes = Column(Integer, nullable=False)
    day_of_the_week = Column(Integer, nullable=False)
