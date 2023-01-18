from functools import wraps

from container.request_context import RequestContext


def transactional(func):
    @wraps(func)
    async def inner(*args, **kwargs):
        db_session = RequestContext.get_request_session()
        async with db_session.begin():
            await func(*args, **kwargs)

    return inner
