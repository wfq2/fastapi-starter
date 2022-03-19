from typing import TypeVar, Type
from uuid import UUID

from sqlalchemy import update, select, insert

from db.current_session import current_session
from .base_dbo import BaseDBO
from .transactional import transactional
from ..exceptions.does_not_exist_exception import DoesNotExistException

T = TypeVar("T", bound=BaseDBO)


class Repository:

    def __init__(self, mapping = None):
        if not mapping:
            from src.db.table_mapping import TableMapping
            mapping = TableMapping
        self.table_mapping = mapping

    @property
    def db_session(self):
        session = current_session.get()
        return session

    async def commit(self):
        await self.db_session.commit()

    def _table(self, dbo: Type[T]):
        return self.table_mapping[dbo.__name__]

    async def insert(self, dbo: T) -> T:
        entry = self._table(dbo.__class__)
        statement = insert(entry).values(**dbo.dict())
        await self.db_session.execute(statement)
        return dbo

    async def update(self, dbo: T) -> None:
        entry = self._table(dbo.__class__)
        statement = update(entry).where(entry.id == dbo.id).values(**dbo.dict())
        await self.db_session.execute(statement)

    async def get(self, dbo: Type[T], id: UUID) -> T:
        entry = self._table(dbo)
        statement = select(entry).where(entry.id == id)
        response = await self.db_session.execute(statement)
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
