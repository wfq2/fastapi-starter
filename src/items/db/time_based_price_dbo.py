from db.base_dbo import BaseDBO


class TimeBasedPriceDBO(BaseDBO):

    price: float
    item_id: str
    start_hour: int
    end_hour: int
    start_minutes: int
    end_minutes: int
    day_of_the_week: int
