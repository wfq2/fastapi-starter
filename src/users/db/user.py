# tables/user.py

from sqlalchemy import Column, String, Boolean

from src.db.base import Base


class User(Base):

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    disabled = Column(Boolean, nullable=False)
    hashed_password = Column(String, nullable=False)
