from uuid import UUID

from fastapi import APIRouter
from kink import di

from src.places.models.place import Place, PlaceOut
from src.places.place_service import PlaceService

router = APIRouter()


@router.get("/api/place", response_model=PlaceOut)
async def get_place(place_id: UUID) -> PlaceOut:
    service = di[PlaceService]
    response = await service.get_place(place_id)
    return PlaceOut(**response.dict())


@router.put("/api/place", response_model=PlaceOut)
async def put_place(place_input: Place) -> PlaceOut:
    service = di[PlaceService]
    response = await service.put_place(place_input)
    return PlaceOut(**response.dict())
