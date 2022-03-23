from datetime import timedelta
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from kink import di

from users.models.create_user_input import CreateUserInput
from users.models.token import Token
from users.models.user import User
from users.models.user_out import UserOut
from users.security_helpers import ACCESS_TOKEN_EXPIRE_MINUTES, oauth2_scheme
from users.security_service import SecurityService
from users.user_service import UserService

router = APIRouter()


@router.get("/api/user", response_model=UserOut)
async def get_place(user_id: UUID) -> UserOut:
    service: UserService = di[UserService]
    response = await service.get_user(user_id)
    return UserOut(**response.dict())


@router.put("/api/user", response_model=User)
async def create_user(user_input: CreateUserInput) -> User:
    service: UserService = di[UserService]
    response = await service.create_user(user_input)
    return response


@router.get("/api/user/me", response_model=User)
async def get_current_user(token: str = Depends(oauth2_scheme)):
    service: SecurityService = di[SecurityService]
    response = await service.get_current_user_by_token(token)
    return response


@router.post("/api/users/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> Token:
    service: SecurityService = di[SecurityService]
    user = await service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # TODO: actually set scopes that the user has
    access_token = service.create_access_token(
        data={"sub": user.email, "scopes": form_data.scopes},
        expires_delta=access_token_expires,
    )
    return Token(**{"access_token": access_token, "token_type": "bearer"})
