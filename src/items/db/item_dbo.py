from typing import List, Optional

from db.base_dbo import BaseDBO
from items.db.time_based_price_dbo import TimeBasedPriceDBO


class ItemDBO(BaseDBO):
    name: str
    description: str
    base_price: float
    time_based_prices: Optional[List[TimeBasedPriceDBO]]

    class Config:
        orm_mode = True
