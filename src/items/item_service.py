from typing import TYPE_CHECKING

from kink import inject
from pydantic.types import UUID
from sqlalchemy import select

from exceptions.does_not_exist_exception import DoesNotExistException
from items.db.item_dbo import ItemDBO
from items.db.time_based_price_dbo import TimeBasedPriceDBO
from items.models.item import Item
from items.models.time_based_price import TimeBasedPrice

if TYPE_CHECKING:
    from src.db.repository import Repository


@inject
class ItemService:
    def __init__(self, repo: "Repository"):
        self.repository = repo

    async def put_item(self, item: Item) -> ItemDBO:
        item_dbo = ItemDBO(**item.dict())
        response = await self.repository.insert(item_dbo)
        await self.repository.commit()
        return response

    async def get_item(self, item_id: UUID) -> ItemDBO:
        table = self.repository.get_table(ItemDBO)
        statement = (
            select(table)
            .where(table.id == item_id)
            .prefetch_related("time_based_prices")
        )
        response = await self.repository.execute(statement)
        item = response.fetchone()[0]
        return ItemDBO.from_orm(item)

    async def put_time_based_price(self, time_based_price: TimeBasedPrice) -> ItemDBO:
        item_dbo = TimeBasedPriceDBO(**time_based_price.dict())
        await self.repository.insert(item_dbo)
        await self.repository.commit()
        table = self.repository.get_table(ItemDBO)
        statement = (
            select(table)
            .where(table.id == item_dbo.item_id)
            .prefetch_related("time_based_prices")
        )
        response = await self.repository.execute(statement)
        response = response.unique()
        if not response:
            raise DoesNotExistException
        return ItemDBO.from_orm(response.fetchone()[0])
