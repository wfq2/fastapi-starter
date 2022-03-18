import asyncio
import time
from typing import Generator

import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.base import Base
from src.db.session import _engine, _async_session


@pytest.fixture(scope="function", autouse=True)
def event_loop(request) -> Generator:
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture()
async def db_session(mocker) -> AsyncSession:
    async with _engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
        await connection.commit()
        async with _async_session(bind=connection) as session:
            mocker.patch("src.db.session.get_session", return_value=session)
            yield session
            await session.flush()
            await session.rollback()
