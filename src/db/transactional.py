
from functools import wraps

from kink import di


def transactional(func):
    @wraps(func)
    async def inner(*args, **kwargs):
        db_session = di["db_session"]
        async with db_session.begin():
            await func(*args, **kwargs)

    return inner
