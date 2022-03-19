from contextvars import ContextVar

current_session = ContextVar("request local session")