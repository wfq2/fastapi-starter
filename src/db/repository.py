from typing import TypeVar, Type
from uuid import UUID

from sqlalchemy import update, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.places.db.place_dbo import PlaceDBO
from .base import Place
from .base_dbo import BaseDBO
from .session import get_session
from .transactional import transactional
from ..exceptions.does_not_exist_exception import DoesNotExistException

T = TypeVar("T", bound=BaseDBO)


class Repository:
    TableMapping = {PlaceDBO.__name__: Place}

    def __init__(self, db_session: AsyncSession):
        self._db_session = db_session if db_session else get_session()

    @property
    def db_session(self):
        return self._db_session

    def commit(self):
        self._db_session.commit()

    def _table(self, dbo: T):
        return self.TableMapping[dbo.__name__]

    async def insert(self, dbo: T) -> T:
        entry = self._table(dbo.__class__)(**dbo.dict())
        self._db_session.add(entry)
        return dbo

    async def update(self, dbo: T) -> None:
        entry = self._table(dbo.__class__)
        statement = update(entry).where(entry.id == dbo.id).values(**dbo.dict())
        await self._db_session.execute(statement)

    async def get(self, dbo: Type[T], id: UUID) -> T:
        entry = self._table(dbo)
        statement = select(entry).where(entry.id == id)
        response = await self._db_session.execute(statement)
        if not response:
            raise DoesNotExistException
        return dbo(**response.fetchone()[0].__dict__)

    @transactional
    async def upsert(self, dbo: Type[T], id: UUID, obj: T) -> T:
        get_response = None
        try:
            get_response = await self.get(dbo, id)
        except DoesNotExistException:
            pass
        to_upsert = obj
        if get_response:
            to_upsert = dbo(**{**obj.dict(), **to_upsert.dict()})
            await self.update(to_upsert)
            return to_upsert
        else:
            await self.insert(to_upsert)
            return to_upsert
