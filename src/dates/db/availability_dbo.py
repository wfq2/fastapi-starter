from db.base_dbo import BaseDBO


class AvailabilityDBO(BaseDBO):

    start_hour: int
    end_hour: int
    start_minutes: int
    end_minutes: int
    day_of_the_week: int
