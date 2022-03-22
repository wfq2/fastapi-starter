from functools import wraps

from kink import di

from db.current_session import current_session


def transactional(func):
    @wraps(func)
    async def inner(*args, **kwargs):
        db_session = current_session.get_by_id()
        async with db_session.begin():
            await func(*args, **kwargs)

    return inner
