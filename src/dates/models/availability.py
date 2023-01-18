"""
0 = sunday, 1=monday, 2=tuesday...
"""
from pydantic import BaseModel, Field


class Availability(BaseModel):
    start_hour: int = Field(..., gte=0, lte=24)
    end_hour: int = Field(..., gte=0, lte=24)
    start_minutes: int = Field(..., gte=0, lte=60)
    end_minutes: int = Field(..., gte=0, lte=60)
    day_of_the_week: int = Field(..., gte=0, lte=6)
