from typing import List
from uuid import UUID

from pydantic import BaseModel


class Place(BaseModel):
    name: str


class PlaceOut(BaseModel):
    id: UUID
    name: str


PlacesResponseType = List[Place]
