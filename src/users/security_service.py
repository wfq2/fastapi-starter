from datetime import datetime, timedelta
from typing import Optional

from fastapi import HTTPException, status
from jose import JWTError, jwt
from kink import inject
from pydantic import ValidationError
from starlette.requests import Request

from exceptions.does_not_exist_exception import DoesNotExistException
from exceptions.invalid_password_exception import InvalidPasswordException
from users.models.token_data import TokenData
from users.models.user import User
from users.security_helpers import SECRET_KEY, ALGORITHM, verify_password, oauth2_scheme
from users.user_service import UserService


@inject
class SecurityService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    async def authenticate_user(self, email: str, password: str) -> Optional[User]:
        try:
            user = await self.user_service.get_user_by_email(email)
        except DoesNotExistException:
            return None
        if not verify_password(password, user.hashed_password):
            raise InvalidPasswordException
        return User(**user.dict())

    async def get_user_from_request(self, request: Request):
        token = await oauth2_scheme(request)
        user = await self.get_current_user_by_token(token)
        return user

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
