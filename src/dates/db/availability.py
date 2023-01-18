from sqlalchemy import Integer, Column

from src.db.base import Base


class Availability(Base):

    start_hour = Column(Integer, nullable=False)
    end_hour = Column(Integer, nullable=False)
    start_minutes = Column(Integer, nullable=False)
    end_minutes = Column(Integer, nullable=False)
    day_of_the_week = Column(Integer, nullable=False)
