from typing import TypeVar, Type
from uuid import UUID

from kink import di
from sqlalchemy.ext.asyncio import AsyncSession

from src.places.db.place_dbo import PlaceDBO
from .base import Place
from .base_dbo import BaseDBO
from .session import get_session

T = TypeVar("T", bound=BaseDBO)


class Repository:
    TableMapping = {PlaceDBO.__name__: Place}

    def __init__(self, db_session: AsyncSession):
        self._db_session = db_session if db_session else get_session()

    def _table(self, dbo: T):
        return self.TableMapping[dbo.__name__]

    async def put(self, dbo: T) -> T:
        entry = self._table(dbo.__class__)(**dbo.dict())
        self._db_session.add(entry)
        await self._db_session.commit()
        return dbo

    async def get(self, dbo: Type[T], id: UUID) -> T:
        response = await self._db_session.get(self._table(dbo), id)
        return dbo(**response.__dict__)
