# base_class.py

import uuid

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: uuid.UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


# import all tables here
from src.db.table_mapping import TableMapping  # noqa: F401,E402

Place = TableMapping["PlaceDBO"]
User = TableMapping["UserDBO"]
Item = TableMapping["ItemDBO"]
