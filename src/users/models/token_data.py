from typing import Optional, List

from pydantic import BaseModel


class TokenData(BaseModel):
    email: Optional[str] = None
    scopes: List[str] = []