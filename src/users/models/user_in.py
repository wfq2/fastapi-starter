from uuid import UUID

from pydantic import BaseModel


class UserIn(BaseModel):
    name: str