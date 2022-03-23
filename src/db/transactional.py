from functools import wraps

from container.request_context import current_session


def transactional(func):
    @wraps(func)
    async def inner(*args, **kwargs):
        db_session = current_session.get_by_id()
        async with db_session.begin():
            await func(*args, **kwargs)

    return inner
