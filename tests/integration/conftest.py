import pytest
import pytest_asyncio
from kink import di
from sqlalchemy.ext.asyncio import AsyncSession

from container.request_context import current_session
from src.db.base import Base
from src.db.repository import Repository
from src.db.session import _engine


@pytest_asyncio.fixture(autouse=True)
async def db_session(mocker) -> AsyncSession:
    async with _engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
        await connection.commit()
    async with di["session_maker"]() as session:
        current_session.set(session)
        yield session
        await session.flush()
        await session.rollback()
    await _engine.dispose()


@pytest.fixture()
def repository() -> "Repository":
    return di[Repository]
