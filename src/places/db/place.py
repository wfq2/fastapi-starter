# tables/place.py

from sqlalchemy import Column, String

from src.db.base import Base


class Place(Base):

    name = Column(String, nullable=False, unique=True)
