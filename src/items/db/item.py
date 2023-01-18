from sqlalchemy import String, Column, Float
from sqlalchemy.orm import relationship

from src.db.base import Base


class Item(Base):

    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    base_price = Column(Float, nullable=True)
    time_based_prices = relationship("TimeBasedPrice")
