import uuid

from pydantic import Field
from pydantic.main import BaseModel
from uuid import UUID


class BaseDBO(BaseModel):
    id: UUID = Field(default_factory=lambda: uuid.uuid4())
