from uuid import UUID

from pydantic import BaseModel


class UserOut(BaseModel):
    id: UUID
    name: str