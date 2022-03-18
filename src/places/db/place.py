# tables/place.py

from sqlalchemy import Column, String

from src.db.base import Base


class Place(Base):
    __tablename__ = "place"

    name = Column(String, nullable=False, unique=True)
