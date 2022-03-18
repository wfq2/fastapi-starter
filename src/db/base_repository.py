import abc
from typing import Generic, TypeVar, Type
from uuid import uuid4, UUID

from sqlalchemy.ext.asyncio import AsyncSession

from .errors import DoesNotExistError
from .base import Base
from ..exceptions.does_not_exist_exception import DoesNotExistException

IN_SCHEMA = TypeVar("IN_SCHEMA", bound=Base)
SCHEMA = TypeVar("SCHEMA", bound=Base)
TABLE = TypeVar("TABLE")


class BaseRepository(Generic[IN_SCHEMA, SCHEMA, TABLE], metaclass=abc.ABCMeta):
    def __init__(self, db_session: AsyncSession, *args, **kwargs) -> None:
        self._db_session: AsyncSession = db_session

    @property
    @abc.abstractmethod
    def _table(self) -> Type[TABLE]:
        ...

    @property
    @abc.abstractmethod
    def _schema(self) -> Type[SCHEMA]:
        ...

    async def create(self, in_schema: IN_SCHEMA) -> SCHEMA:
        entry = self._table(id=uuid4(), **in_schema.dict())
        self._db_session.add(entry)
        await self._db_session.commit()
        return self._schema.from_orm(entry)

    async def get_by_id(self, entry_id: UUID) -> SCHEMA:
        entry = await self._db_session.get(self._table, entry_id)
        if not entry:
            raise DoesNotExistException(
                f"{self._table.__name__}<id:{entry_id}> does not exist"
            )
        return self._schema.from_orm(entry)
