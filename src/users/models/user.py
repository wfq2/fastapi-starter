from typing import List

from db.base_dbo import BaseDBO


class User(BaseDBO):
    first_name: str
    last_name: str
    email: str
    disabled: bool = False
    scopes: List[str] = []


anonymous_user = User(
    first_name="ANONYMOUS", last_name="ANONYMOUS", email="ANONYMOUS", disabled=False
)
