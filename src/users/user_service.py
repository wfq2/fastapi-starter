from uuid import UUID

from kink import inject
from typing import TYPE_CHECKING

from passlib.context import CryptContext

from users.db.user_dbo import UserDBO
from users.models.create_user_input import CreateUserInput
from users.models.user import User
from users.models.user_in import UserIn

if TYPE_CHECKING:
    from src.db.repository import Repository


@inject
class UserService:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __init__(self, repo: "Repository"):
        self.repository = repo

    async def get_user(self, id: UUID) -> UserDBO:
        db_response = await self.repository.get_by_id(UserDBO, id)
        return db_response

    async def get_user_by_email(self, email: str) -> UserDBO:
        db_response = await self.repository.get_by_field(UserDBO, "email", email)
        return db_response

    async def create_user(self, user: CreateUserInput) -> User:
        hashed_password = self.pwd_context.hash(user.password)
        user_dbo = UserDBO(**user.dict(), hashed_password=hashed_password)
        response = await self.repository.insert(user_dbo)
        await self.repository.commit()
        return User(**response.dict())
