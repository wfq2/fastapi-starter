import asyncio
from contextvars import ContextVar

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_scoped_session
from sqlalchemy.orm import sessionmaker

from src.config import settings

_engine = create_async_engine(
    settings.async_database_url,
    echo=settings.DB_ECHO_LOG,
)

_async_session = sessionmaker(_engine, class_=AsyncSession, expire_on_commit=False)


def get_session():
    return async_scoped_session(_async_session, scopefunc=asyncio.current_task)()
