from contextlib import contextmanager

from kink import di

from src.db.repository import Repository


@contextmanager
async def session_scope():
    """Provide a transactional scope around a series of operations."""
    repository = di[Repository]
    async with repository._db_session.begin() as s:
        try:
            yield s
            s.commit()
        except:
            s.rollback()
            raise
