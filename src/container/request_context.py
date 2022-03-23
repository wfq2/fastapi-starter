from contextvars import ContextVar
from typing import Any

from users.models.user import User

current_user: Any = ContextVar("request local user")

current_session: Any = ContextVar("request local session")


class RequestContext:
    @staticmethod
    def get_request_session():
        return current_session.get()

    @staticmethod
    def set_request_session(session):
        return current_session.set(session)

    @staticmethod
    def get_request_user():
        return current_user.get()

    @staticmethod
    def set_request_user(user: User):
        current_user.set(user)
