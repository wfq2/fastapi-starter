from datetime import datetime, timedelta
from typing import Optional, TYPE_CHECKING

from fastapi import HTTPException, status
from fastapi.security import (
    OAuth2PasswordBearer,
)
from jose import JWTError, jwt
from kink import inject
from passlib.context import CryptContext
from pydantic import ValidationError

# to get a string like this run:
# openssl rand -hex 32
from exceptions.does_not_exist_exception import DoesNotExistException
from exceptions.invalid_password_exception import InvalidPasswordException
from users.models.token_data import TokenData
from users.models.user import User
from users.user_service import UserService

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"



@inject
class SecurityService:

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    async def authenticate_user(self, email: str, password: str) -> Optional[User]:
        try:
            user = await self.user_service.get_user_by_email(email)
        except DoesNotExistException:
            return None
        if not self.verify_password(password, user.hashed_password):
            raise InvalidPasswordException
        return User(**user.dict())

    async def get_current_user_by_token(self, token: str) -> User:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            email: str = payload.get("sub")
            if email is None:
                raise credentials_exception
            token_scopes = payload.get("scopes", [])
            token_data = TokenData(scopes=token_scopes, email=email)
        except (JWTError, ValidationError):
            raise credentials_exception
        user = await self.user_service.get_user_by_email(token_data.email)
        if user is None:
            raise credentials_exception
        return User(**user.dict())

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return cls.pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return cls.pwd_context.hash(password)

    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
