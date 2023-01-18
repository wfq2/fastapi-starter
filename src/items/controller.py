from uuid import UUID

from fastapi import APIRouter
from kink import di

from items.item_service import ItemService
from items.models.item import ItemOut, Item
from items.models.time_based_price import TimeBasedPrice

router = APIRouter()


@router.put("/api/item", response_model=ItemOut)
async def put_item(item: Item) -> ItemOut:
    service: ItemService = di[ItemService]
    response = await service.put_item(item)
    return ItemOut(**response.dict(exclude_none=True))


@router.get("/api/item", response_model=ItemOut)
async def get_item(item_id: UUID) -> ItemOut:
    service: ItemService = di[ItemService]
    response = await service.get_item(item_id)
    return ItemOut(**response.dict(exclude_none=True))


@router.put("/api/time_based_price", response_model=ItemOut)
async def put_time_based_price(time_based_price: TimeBasedPrice) -> ItemOut:
    service: ItemService = di[ItemService]
    response = await service.put_time_based_price(time_based_price)
    return ItemOut(**response.dict())
