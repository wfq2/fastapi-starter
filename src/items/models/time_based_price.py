from pydantic import BaseModel


class TimeBasedPrice(BaseModel):
    price: float
    item_id: str
    start_hour: int
    end_hour: int
    start_minutes: int
    end_minutes: int
    day_of_the_week: int
