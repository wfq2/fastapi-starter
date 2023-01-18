from typing import List
from uuid import UUID

from pydantic import BaseModel

from items.models.time_based_price import TimeBasedPrice


class Item(BaseModel):
    name: str
    description: str
    base_price: float
    # time_base_prices: List[TimeBasedPrice] = []


class ItemIn(BaseModel):
    name: str
    description: str
    base_price: float
    # time_base_prices: List[TimeBasedPrice]


class ItemOut(BaseModel):
    id: UUID
    name: str
    description: str
    base_price: float
    time_based_prices: List[TimeBasedPrice] = []
