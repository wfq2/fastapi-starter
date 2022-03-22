from pydantic import BaseModel


class CreateUserInput(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
