from uuid import UUID

from kink import inject
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.db.repository import Repository
from src.places.db.place_dbo import PlaceDBO
from src.places.models.place import Place


@inject
class PlaceService:
    def __init__(self, repo: "Repository"):
        self.repository = repo

    async def get_place(self, id: UUID) -> PlaceDBO:
        db_response = await self.repository.get_by_id(PlaceDBO, id)
        return db_response

    async def put_place(self, place: Place) -> PlaceDBO:
        place_dbo = PlaceDBO(**place.dict())
        response = await self.repository.insert(place_dbo)
        await self.repository.commit()
        return response
